for linha in open("/var/log/auth.log"):
    if "Failed password" in linha:
        partes = linha.split()
        i = partes.index("for")
        if partes[i+1] == "invalid":
            usuario = partes[i+3]
        else:
            usuario = partes[i+1]
        metodo = "ssh" if "sshd" in linha else "su" if "su:" in linha else "outro"
        print(usuario, metodo)