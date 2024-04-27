{ lib
,pkgs
,buildPythonPackage
}:

buildPythonPackage rec
  {
    version = "0.1.0";
    
    buildInputs = with pkgs; [
        playerctl
    ];

    src = ./.;

    meta = with lib; {
      description = "rich-presence of your music players";
      homepage = "https://github.com/bramtechs/music-rpc";
      license = licenses.mit;
      maintainers = with maintainers; [ bramtechs ];
    };
  }

