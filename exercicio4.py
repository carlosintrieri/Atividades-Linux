import subprocess

print("Verificando logins rejeitados (não relacionados a senha incorreta)...\n")

saida = subprocess.getoutput("journalctl -t sshd -t sudo --no-pager")

total = 0
for linha in saida.splitlines():
    baixa = linha.lower()
    if "invalid user" in baixa or "not in the sudoers" in baixa or "permission denied" in baixa:
        print(f" {linha}")
        total += 1

print(f"\nTotal de rejeições encontradas: {total}")