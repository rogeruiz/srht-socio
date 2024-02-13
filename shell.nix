with import <nixpkgs> { };

let
  pythonPackages = python311Packages;
in

pkgs.mkShell /* rec */ {
  name = "gen-social";
  venvDir = "./.venv";
  buildInputs = [
    pythonPackages.python
    pythonPackages.venvShellHook
    pythonPackages.click
    pythonPackages.wand
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
          "Playfair Display"
        ];
      })
      (nerdfonts.override { fonts = [ "FantasqueSansMono" ]; })
    ];
  };

  postVenvCreation = ''
    unset SOURCE_DATE_EPOCH
    pip install -r requirements.txt
  '';

  postShellHook = ''
    # allow pip to install wheels
    unset SOURCE_DATE_EPOCH
  '';
}
