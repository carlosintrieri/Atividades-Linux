import subprocess

print("Verificando servicos iniciados ou parados...\n")

saida = subprocess.getoutput("journalctl --no-pager")

total = 0
for linha in saida.splitlines():
    if "Started " in linha or "Stopped " in linha:
        print(linha)
        total += 1

print(f"\nTotal de eventos de servico encontrados: {total}")