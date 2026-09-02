import subprocess
saida = subprocess.getoutput("last -F")
for linha in saida.splitlines():
    if "reboot" in linha or "wtmp" in linha or linha.strip() == "":
        continue
    partes = linha.split()
    usuario = partes[0]
    duracao = [p for p in partes if p.startswith("(")]
    if duracao:
        print("Usuario:", usuario, "Tempo logado:", duracao[0])