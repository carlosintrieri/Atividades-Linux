servico = "kernel"

for linha in open("/var/log/syslog"):
    if servico in linha and ("error" in linha.lower() or "warning" in linha.lower()):
        print(linha.strip())


    # com kernel, aparece uma grande lista. com sshd, não havia conteúdo. por isso optei por kernel como serviço!