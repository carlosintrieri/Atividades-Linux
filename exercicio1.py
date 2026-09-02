import sys
from collections import Counter
 
arquivo = sys.argv[1]
 
falhas = []
sucesso = []
 
for linha in open(arquivo):
    if "Failed password" in linha:
        falhas.append(linha.split()[8])
    elif "Accepted" in linha:
        p = linha.split()
        sucesso.append(f"{p[0]} {p[1]} {p[2]} - {p[8]}")
 
print("=== Tentativas de login FALHAS ===")
for usuario, qtd in Counter(falhas).most_common():
    print(f"{usuario}: {qtd} tentativa(s)")