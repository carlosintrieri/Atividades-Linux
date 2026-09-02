import subprocess

print("Verificando eventos de shutdown/reinicializacao...\n")

saida = subprocess.getoutput("journalctl --no-pager")

total = 0
for linha in saida.splitlines():
    baixa = linha.lower()
    if "shutdown" in baixa or "reboot" in baixa or "powering down" in baixa:
        print(linha)
        total += 1

print(f"\nTotal de eventos encontrados: {total}")