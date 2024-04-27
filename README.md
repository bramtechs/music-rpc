# music-rpc
## One Python script to rule them all!

music-rpc is a simple python script that displays rich-presence of your music player on your Discord profile.
Currently supported music players are:
- Audacious
- Rhythmbox
- cmus
- sayonara
- spotify

Ubuntu/Debian
```bash
sudo apt install playerctl

python3 -m venv ./venv
./venv/bin/pip3 install -r requirements.txt
./venv/bin/python3 ./scan.py 
```

NixOS
```bash
nix-shell
```
or download from [my nix channel](https://github.com/bramtechs/nix-channel)
```
nix-shell -p music-rpc
```

## Screenshot
![examples](screenshots/examples.png "examples")
