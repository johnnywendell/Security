#comparador de hashes comparador de criptografia
import hashlib

arquivo1 = 'c:/workspace/SEGURANÇA/Ferramentas/comparar hashes/a.txt'
arquivo2 = 'c:/workspace/SEGURANÇA/Ferramentas/comparar hashes/b.txt'

hash1 = hashlib.new('ripemd160') #Aqui você diz qual algoritmo de hash vai usar ex: md5, sha1, sha256, e etc...
hash1.update(open(arquivo1, 'rb').read())#O update faz a comparação

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

# digest resume os dados passados pelo update

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.digest())
    print('O hash do arquivo b.txt é: ', hash2.digest())
else:
    print(f'O arquivo: {arquivo1} é igual do {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())

