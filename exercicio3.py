import subprocess
 
print("Auditando uso do sudo...\n")
 
saida = subprocess.getoutput("journalctl -t sudo --no-pager")
 
total = 0
for linha in saida.splitlines():
    if "COMMAND=" in linha:
        print(f"{linha}")
        total += 1
 
print(f"\nTotal de comandos sudo encontrados: {total}")
 