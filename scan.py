
import utils
import json
import session
from time import sleep

busy_session : session.Session = None
config : dict

def player_is_valid(player_name: str) -> bool:
    for player in config["players"]:
        if player_name == player:
            return True
    return False

def check_players():
    # check if already busy with a session
    global busy_session
    if busy_session != None:
        return False
    # Check if any players are playing
    act_players = utils.execute("playerctl -l").split('\n')
    for player in act_players:
        if player_is_valid(player):
            busy_session = session.Session(player,config["players"][player])
            print("done")
            busy_session = None
            return True
    # no valid player, keep searching

if __name__ == '__main__':
    print("music-rpc started... " + utils.execute('date'))

    with open("players.json","r") as json_file:
        config = json.load(json_file)
        print (json_file.readlines)
    print("Loaded config...")

    while True:
        check_players()
        sleep(3)