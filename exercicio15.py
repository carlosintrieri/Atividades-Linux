total_linhas = 0
total_com_t = 0
total_no_intervalo = 0

inicio = "10:00:00"
fim = "11:00:00"

for linha in open("/var/log/syslog"):
    total_linhas += 1
    partes = linha.split("T")
    if len(partes) < 2:
        continue
    total_com_t += 1
    hora = partes[1][:8]
    if inicio <= hora < fim:
        total_no_intervalo += 1
        print(linha.strip())

print("---")
print("Linhas lidas:", total_linhas)
print("Linhas com T:", total_com_t)
print("Linhas no intervalo:", total_no_intervalo)