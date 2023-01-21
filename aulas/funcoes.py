def linha(): #para definir uma função no python é def de definir
    print('-' *30)
linha()
print('Seja bem vindo!')
linha()
def somar(n1, n2): #parâmetros funcionam como variaveis para informar o que fazer com as informações recebidas
    return print(f'O número {n1} somado ao número {n2} resulta em {n1+n2}\n')
somar(78,302) #n1 = 78        n2 = 30
def enum(n = 0): #usando parâmetro = 0 ou qual quer valor, esse valor é atribuido 
    n = input('Digite um número por favor: ')
    while True:
        if n.isnumeric():
            break
        else:
            n = input('Digite um número sem letras, por favor: ')
    return int(n) #return retorna um valor a função
n1 = 0
n2 = 0
somar(enum(n1),enum(n2))
