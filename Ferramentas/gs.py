#GERADOR DE SENHAS
import random, string

tamanho = int(input("digite o tamanho da senha que deseja criar: "))

chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+,.;:/?'

rnd = random.SystemRandom() #os.urandom a função system chama essa classe dessa biblioteca
# (gera numeros aleatórios apartir de fontes fornecidas pelo sistema operacional

print(''.join(rnd.choice(chars) for i in range(tamanho)))