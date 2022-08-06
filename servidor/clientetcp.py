import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)#AF para dizer que é IP,
        # STREAM pra dizer que é PROTOCOLO TCP
    except socket.error as e:
        print("conexão falhou")
        print("Erro: {}".format(e))
        sys.exit()
    print("Socket criado com sucesso!")

    HostAlvo =  input("Digite o Host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente conectado com sucesso: ")
        s.shutdown(2)
    except socket.error as e:
        print("não foi possível conectar")
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == '__main__':
    main()
