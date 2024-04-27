{ pkgs ? import <nixpkgs> {} }:

let
  def = pkgs.callPackage ./default.nix {};
in pkgs.mkShell
  {
    buildInputs = [
      def
    ];

    shellHook = ''
      music-rpc
    ''; 
  }
