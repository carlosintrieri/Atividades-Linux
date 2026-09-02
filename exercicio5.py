import subprocess

print("Verificando o último boot do sistema...\n")

saida = subprocess.getoutput("who -b")

print(f"⏱{saida}")