#Verificador de IP externo
import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

response = urlopen(url)

dados = json.load(response)

ip = dados['ip']
city = dados['city']
hostname = dados['hostname']

print('ip = {}\ncity = {}\nhostname = {}'.format(ip, city, hostname))