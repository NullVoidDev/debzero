#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys


def run_command(command: list[str]) -> int:
    """Executa um comando e retorna o código de saída."""
    try:
        result = subprocess.run(command, check=False)
        return result.returncode
    except FileNotFoundError:
        print(f"Erro: comando não encontrado: {' '.join(command)}")
        return 1


def install_deb(deb_path: str) -> int:
    """Instala um pacote .deb usando dpkg e corrige dependências com apt-get."""
    if not os.path.isfile(deb_path):
        print(f"Erro: arquivo '{deb_path}' não encontrado.")
        return 1

    if not deb_path.endswith(".deb"):
        print(f"Atenção: '{deb_path}' não termina com '.deb'. Continuando mesmo assim...")

    print(f"\n==> Instalando pacote: {deb_path}")
    exit_code = run_command(["sudo", "dpkg", "-i", deb_path])

    if exit_code != 0:
        print("Falha na instalação com dpkg. Tentando corrigir dependências com 'sudo apt-get -f install -y'...")
        fix_code = run_command(["sudo", "apt-get", "-f", "install", "-y"])
        if fix_code != 0:
            print("Erro: não foi possível corrigir dependências automaticamente.")
            return fix_code

        # Tenta novamente instalar o pacote após corrigir dependências
        print("Tentando novamente instalar o pacote...")
        exit_code = run_command(["sudo", "dpkg", "-i", deb_path])

    if exit_code == 0:
        print("Instalação concluída com sucesso.")
    else:
        print("A instalação falhou.")

    return exit_code


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Instala arquivos .deb usando dpkg e corrige dependências com apt-get."
    )
    parser.add_argument(
        "debs",
        nargs="+",
        help="Um ou mais caminhos para arquivos .deb a serem instalados",
    )

    args = parser.parse_args(argv)

    codes: list[int] = []
    for deb in args.debs:
        code = install_deb(deb)
        codes.append(code)

    # resumo
    print("\nResumo:")
    for deb, code in zip(args.debs, codes):
        status = "OK" if code == 0 else f"ERRO (código {code})"
        print(f"  - {deb}: {status}")

    # se qualquer um falhar, retorna 1
    return 0 if all(c == 0 for c in codes) else 1


if __name__ == "__main__":
    raise SystemExit(main())

