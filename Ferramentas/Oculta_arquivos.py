import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('arquivoParaOcultar.txt', atributo_ocultar)

if retorno:
    print('Arquivo foi ocultado')
else:
    print("arquivo não foi ocultado")
