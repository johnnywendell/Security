import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('servidor socket criado com sucesso')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = '\nOláaaaa Cliente e ai beleza?'

while 1:# um é verdadeiro 0 é falso o bind retorna verdadeiro ou falso

    dados, end = s.recvfrom(4096)
    if dados:

        print('servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)
