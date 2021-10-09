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

    def get_end_time(self) -> str:
        position = int(utils.execute(self.cmd_prefix+"metadata --format \"{{position}}\""))*0.000001
        length = int(utils.execute(self.cmd_prefix+"metadata --format \"{{mpris:length}}\""))*0.000001
        return time.time()+length-position

    def refresh(self,config):
        self.side = not self.side
        details = self.get_song_details()
        state = self.get_song_state()
        player_state = self.get_player_state()
        if player_state == "Playing":
            end_time = self.get_end_time()
        elif player_state == "No players found" or player_state == '':
            self.running = False
            return
        else:
            end_time = 0
        large_image = config["logo"]
        small_image = config[player_state]
        discord_rpc.update_presence(
            **{
                'state': state,
                'details': details,
                'end_timestamp': end_time,
                'large_image_key': large_image,
                'small_image_key': small_image
            })
        discord_rpc.update_connection()
        time.sleep(2)
        discord_rpc.run_callbacks()

    def shutdown(self):
        print ("Player stopped ending session...")
        discord_rpc.shutdown()
