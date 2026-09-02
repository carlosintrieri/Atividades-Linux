import subprocess

saida = subprocess.getoutput("journalctl -t sudo --no-pager")

for linha in saida.splitlines():
    if "COMMAND=" in linha and ("apt" in linha or "dpkg" in linha):
        print(linha)