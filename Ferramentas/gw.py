#GERA WORDLISTS (todas combinações possíveis com os caracteres escolhidos
import itertools

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))