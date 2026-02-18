# debzero

Script simples em Python para facilitar a instalação de pacotes `.deb` no Pop!\_OS/Ubuntu.

## Funcionalidades

- Instala um ou mais arquivos `.deb` usando `dpkg`.
- Tenta corrigir dependências automaticamente com `apt-get -f install`.
- Mostra um resumo final com sucesso/erro de cada arquivo.

## Requisitos

- Python 3
- `dpkg` e `apt-get` (presentes na maioria das distros baseadas em Debian/Ubuntu)

## Uso

No diretório do projeto:

```bash
cd ~/Documentos/debzero
python3 debzero.py arquivo.deb
```

Também aceita vários arquivos de uma vez:

```bash
python3 debzero.py arquivo1.deb arquivo2.deb arquivo3.deb
```

### Alias conveniente (`debzero`)

Para poder chamar o script de qualquer lugar com o comando `debzero`, adicione este alias ao final do seu `~/.bashrc`:

```bash
echo "alias debzero='python3 ~/Documentos/debzero/debzero.py'" >> ~/.bashrc
source ~/.bashrc
```

Depois disso é só usar:

```bash
debzero arquivo.deb
debzero arquivo1.deb arquivo2.deb
```

## Estrutura do projeto

- `debzero.py` — script principal em Python.
- `README.md` — documentação do projeto.
- `requirements.txt` — dependências Python (atualmente sem libs externas).

