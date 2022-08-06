#multiplos threadins processos ao mesmo tempo
from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 50:
        print('piloto: {} km: {} \n'.format(piloto, trajeto))
        trajeto += velocidade
        time.sleep(1.0)


t_carro1 = Thread(target=carro, args=[10, 'Johnny'])
t_carro2 = Thread(target=carro, args=[20, 'Python'])

t_carro1.start()
t_carro2.start()

