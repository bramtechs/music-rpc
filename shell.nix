{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell
{
    nativeBuildInputs = with pkgs; [
        playerctl
        python3
        python311Packages.pip
    ];

    shellHook = ''
      python -m venv venv --copies
      ./venv/bin/pip3 install discord-rpc.py
      ./venv/bin/python3 ./scan.py
    '';
}
