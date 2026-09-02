import subprocess

processo = subprocess.Popen(["tail", "-f", "/var/log/auth.log"], stdout=subprocess.PIPE, text=True)

for linha in processo.stdout:
    if "Failed password" in linha:
        print(linha.strip())


        # neste caso, entrar com usuário falso em outro terminal para brecar o login do código