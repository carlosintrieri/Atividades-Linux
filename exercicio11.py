from datetime import datetime, timedelta

limite = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

for linha in open("/var/log/dpkg.log"):
    if " install " in linha and linha[:10] >= limite:
        print(linha.strip())