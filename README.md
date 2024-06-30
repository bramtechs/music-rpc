# music-rpc
## One Python script to rule them all!

music-rpc is a simple Python script that displays Discord rich-presence for the following music players:
- Audacious
- Rhythmbox
- cmus
- sayonara
- spotify

This script needs **playerctl** and the pip3 library **discord_rpc.py** in order to function. Make sure they are installed!

Ubuntu/Debian
```bash
sudo apt install playerctl -y
python3 -m venv ./venv
./venv/bin/pip3 install discord-rpc.py
./venv/bin/python3 ./scan.py
```

NixOS
```bash
nix-shell
```

## Screenshot
![examples](screenshots/examples.png "examples")
