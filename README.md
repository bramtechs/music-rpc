# music-rpc
## One Python script to rule them all!

music-rpc is a simple python script that displays rich-presence of your music player on your discord profile.
Currently supported music players are:
- Audacious
- Rhythmbox
- cmus
- sayonara
- ...
- spotify *(don't ask)*

This script needs **playerctl** and the pip3 library **discord_rpc.py** in order to function. Make sure they're installed!

Ubuntu/Debian
```bash
sudo apt install playerctl
pip3 install discord-rpc.py
python3 ./scan.py
```

NixOS
```bash
nix-shell
```

### UPDATE (future Debian):
Debian has changed the way pip works by forcing you to use virtual environments. Create one with the following commands:
```bash
# create a virtual environment with venv
python3 -m venv ./venv
./venv/bin/pip3 install discord-rpc.py
# then run the script with
./venv/bin/python3 ./scan.py 
```

## Screenshot
![examples](screenshots/examples.png "examples")
