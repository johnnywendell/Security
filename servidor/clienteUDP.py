import socket
import sys



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#AF para dizer que é IP,
# DGRAM pra dizer que é PROTOCOLO TCP
print('cliente socket criado com sucesso')

host = 'localhost'
porta = 5433
mensagem = 'olá servidor firmeza?'

try:
    print('Cliente:' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(dados)
finally:
    print('Cliente: Fechando a conexão')
    s.close()
