import re

with open('/tmp/darkweb2017-top10000.txt') as f:
    for password in f.readlines():

        password = password.strip()

        if len(password) < 12:
            continue

        if len(re.findall(r'[a-z]', password)) < 1:
            continue

        if len(re.findall(r'[A-Z]', password)) < 1:
            continue

        if len(re.findall(r'\d', password)) < 1:
            continue

        print(password)

