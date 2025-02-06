#!/usr/bin/env bash

python3 -m venv ./venv
./venv/bin/pip3 install discord-rpc.py

SERVICE_NAME="musicrpc.service"
SERVICE_PATH="$PWD/$SERVICE_NAME"
SYMLINK_PATH="$HOME/.config/systemd/user/$SERVICE_NAME"

mkdir -p "$HOME/.config/systemd/user"

cat <<EOF > "$SERVICE_PATH"
[Unit]
Description=MusicRPC
After=network.target

[Service]
ExecStart=$PWD/venv/bin/python3 ./scan.py
WorkingDirectory=$PWD
Restart=always
RestartSec=5
StartLimitBurst=5

StandardOutput=journal
StandardError=journal

[Install]
WantedBy=default.target
EOF

ln -sf "$SERVICE_PATH" "$SYMLINK_PATH"

systemctl --user daemon-reload
systemctl --user enable "$SERVICE_NAME"
systemctl --user status "$SERVICE_NAME"

echo "Systemd service file created and symlinked successfully."
