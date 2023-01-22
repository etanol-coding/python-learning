def inputword(msg): #um input que só aceita palavras
    while True:
            nome = input(msg).strip().capitalize()
            if nome.isalpha():
                break
            else:
                print('Digite somente com letras, por favor.')
    return nome
def ola(): #pergunta o nome do usuario e da boas vindas
    nome = inputword('Digite seu nome por favor: ')
    print(f'Olá! Tudo bem com você {nome}?')