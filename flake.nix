{
  description = "simple python devshell flake for data structures and algorithms / leetcode prep in python!";
  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" ];
      forAllSystems = f: nixpkgs.lib.genAttrs systems (system: f nixpkgs.legacyPackages.${system});
    in {
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          buildInputs = [
            pkgs.ruff
            pkgs.uv

            (pkgs.python313.withPackages (ps: [
              ps.pytest
            ]))
          ];

          shellHook = ''
            echo "python: $(python --version)"
            echo "uv: $(uv --version)"
          '';
        };
      });
    };
}
