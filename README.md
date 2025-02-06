# music-rpc
## One Python script to rule them all!

music-rpc is a simple Python script that displays Discord rich-presence for the following music players:
- Audacious
- Rhythmbox
- cmus
- sayonara
- spotify

This script needs **playerctl** and the pip3 library **discord_rpc.py** in order to function. Make sure they are installed!

## Manually

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

## As a user SystemD service

Ensure playerctl is installed.

```
chmod +x install-systemd-server.sh
./install-systemd-server.sh
```

## Screenshot
![examples](screenshots/examples.png "examples")
