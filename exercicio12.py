for linha in open("/var/log/dpkg.log"):
    if " remove " in linha:
        print(linha.strip())