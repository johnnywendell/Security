#trabalhar com ips
import ipaddress

ip = '192.168.0.1'

rede = "192.168.0.0/32"

endereco = ipaddress.ip_address(ip)
endereco_rede = ipaddress.ip_network(rede, strict=False)
#print(endereco)
#print(endereco_rede)

for rede in endereco_rede:
    print(rede)