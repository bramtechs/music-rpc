import discord_rpc
import time
import utils

def on_ready(current_user):
    print('Our user: {}'.format(current_user))


def on_disconnect(codeno, codemsg):
    print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
        codeno, codemsg))


def on_error(errno, errmsg):
    print('An error occurred! Error {}: {}'.format(errno, errmsg))


class Session:
    def __init__(self, player_name: str, config: dict) -> None:
        print("Opening session on player " + player_name)
        self.player_name = player_name
        self.cmd_prefix = "playerctl -p " + self.player_name + " "
        print("Starting discord session... " + config["appID"])
        callbacks = {
            'ready': on_ready,
            'disconnected': on_disconnect,
            'error': on_error,
        }

        # setup the session with correct settings
        discord_rpc.initialize(app_id=config["appID"],
                               callbacks=callbacks,
                               log=True,log_file="discord_log.txt")
        
        self.large_image = config["logo"]
        print("set logo to " + config["logo"])
        self.details = "Initializing player " + player_name
        self.state = "state"
        self.small_image = config["Stopped"]
        self.side = False
        self.refresh(config)
        self.running = True

        while self.running:
            time.sleep(3)
            self.refresh(config)
        self.shutdown()

    def get_song_details(self) -> str:
        result = ""
        album = utils.execute(self.cmd_prefix + "metadata --format \"{{album}}\"")
        title = utils.execute(self.cmd_prefix + "metadata --format \"{{title}}\"")
        
        # Avoid Unknown album tag on rhythmbox
        if album == "Unknown":
            album = ""

        if len(album) == 0 or len(title) == 0 or len(album) < 16 and len(title) < 16:
            result = title
            if len(album) > 0:
                result += " - " + album
        elif self.side:
            result = title
        else:
            result = album
        return result

    def get_song_state(self) -> str:
        artist = utils.execute(self.cmd_prefix + "metadata --format \"{{artist}}\"")
        # Avoid Unknown artist tag on rhythmbox
        if artist == "Unknown":
            artist = ""
        return artist

    def get_player_state(self) -> str:
        return utils.execute(self.cmd_prefix + "status")

    def get_length(self) -> int:
        length_text = utils.execute(self.cmd_prefix+"metadata --format \"{{mpris:length}}\"")
        if (length_text != ""): # if not listening to icecast livestream (length not null)
            return int(length_text)*0.000001
        return -1 # unlimited length

    def get_position(self) -> int:
        return int(utils.execute(self.cmd_prefix+"metadata --format \"{{position}}\""))*0.000001

    def refresh(self,config):
        self.side = not self.side
        details = self.get_song_details()
        state = self.get_song_state()
        player_state = self.get_player_state()
        end_time = -1
        if player_state == "Playing":
            if self.get_length() != -1:
                end_time = time.time()+self.get_length()-self.get_position() # get end time
        elif player_state == "No players found" or player_state == '':
            self.running = False
            return
        large_image = config["logo"]
        small_image = config[player_state]
        if end_time > 0:
            discord_rpc.update_presence(
                **{
                    'state': state,
                    'details': details,
                    'start_timestamp':0,
                    'end_timestamp': end_time,
                    'large_image_key': large_image,
                    'small_image_key': small_image
                })
        else:
            discord_rpc.update_presence(
                **{
                    'state': state,
                    'details': details,
                    'start_timestamp': time.time()-self.get_position(),
                    'end_timestamp':0,
                    'large_image_key': large_image,
                    'small_image_key': small_image
                })
        discord_rpc.update_connection()
        time.sleep(2)
        discord_rpc.run_callbacks()

    def shutdown(self):
        print ("Player stopped ending session...")
        discord_rpc.shutdown()
