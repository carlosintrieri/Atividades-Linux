import subprocess

saida = subprocess.getoutput("last")

print("🔎 Verificando logins bem-sucedidos...\n")

total = 0
for linha in saida.splitlines():
    if linha.strip() == "" or "wtmp begins" in linha or "reboot" in linha:
        continue
    p = linha.split()
    usuario = p[0]
    print(f" Usuário: {usuario} - {linha}")
    total += 1

print(f"\n Fim da análise! {total} login(s) encontrado(s). Até a próxima!")