import os, time

with open('c:\workspace\SEGURANÇA\ping\hosts.txt') as file:
    dump = file.read()
    print(dump)
    dump = dump.splitlines()

    for ip in dump:
        os.system('ping -n 2 '+ ip)
        time.sleep(5)