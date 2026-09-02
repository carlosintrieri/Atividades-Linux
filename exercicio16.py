from collections import Counter

servicos = []

for linha in open("/var/log/syslog"):
    partes = linha.split()
    if len(partes) >= 5:
        nome = partes[4].split("[")[0].rstrip(":")
        servicos.append(nome)

for servico, qtd in Counter(servicos).most_common(10):
    print(f"{servico:<20} {qtd}")