def parImpar (numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'

entrada = input('Digite um número: ')

try:
    numero = int(entrada)
    resultado = parImpar(numero)
    print(f'O número {numero} é {resultado}')
except: 
    print('Erro: Digite um número inteiro')
