#gera hashs (criptografia)
import hashlib

string = input("Digite o texto a ser criptografado: ")

menu = int(input(''' ####MENU - ESCOLHAO TIPO DE HASH ###
                            1) MD5
                            2) SHA1
                            3) SHA256
                            4) SHA512
                            Digite o número do hash a ser gerado: '''))
if menu == 1:
    resultado = hashlib.md4(string.encode('utf-8'))
    print('o hash MD5 da string ', string, 'é: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('o hash SHA1 da string ', string, 'é: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('o hash SHA256 da string ', string, 'é: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('o hash SHA512 da string ', string, 'é: ', resultado.hexdigest())
else:
    print('Algo de rerrado não deu certo, tente novamente')