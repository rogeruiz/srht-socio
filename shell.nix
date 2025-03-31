with import <nixpkgs> { };

let
  pythonPackages = python311Packages;
in

pkgs.mkShell # rec
  {
    name = "socio";
    venvDir = "./.venv";
    buildInputs = [
      pythonPackages.python
      pythonPackages.venvShellHook
      # pythonPackages.click
      # pythonPackages.wand
      # pythonPackages.pydantic
      pythonPackages.build
      pythonPackages.setuptools

      pythonPackages.python-lsp-server

      imagemagick
    ];

    FONTCONFIG_FILE = makeFontsConf {
      fontDirectories = with pkgs; [
        (google-fonts.override {
          fonts = [
            "Quattrocento"
            "Abril Fatface"
          ];
        })
        (nerdfonts.override { fonts = [ "Recursive" ]; })
      ];
    };

    postVenvCreation = ''
      unset SOURCE_DATE_EPOCH
      pip install -r requirements.txt
    '';

    postShellHook = ''
      # allow pip to install wheels
      unset SOURCE_DATE_EPOCH
      export MAGICK_HOME="${pkgs.imagemagick}"
    '';
  }
