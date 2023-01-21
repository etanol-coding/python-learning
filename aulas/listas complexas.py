galera = list()
pessoa = list()
primeiravez = True
while True:
    nome = input('Digite o nome: ').strip().capitalize()
    while True:
        if nome.isalpha():
            break
        else:
            nome = input('Digite em letras, por favor: ').strip().capitalize()
    pessoa.append(nome)
    idade = input('Digite a idade: ').strip()
    while True:
        if idade.isnumeric():
            break
        else:
            idade = int(input('Digite em números, por favor: ')).strip()
    pessoa.append(idade)
    galera.append(pessoa[:]) #sempre que for colocar uma lista em outra pelo append utilize [:]
    pessoa.clear()
    if input('Você deseja continuar? S/N --->  ').upper().strip() == 'N':
        break
pc = len(galera)
print('Apenas uma pessoa foi cadastrada hoje.' if pc == 1 else f'Hoje {pc} pessoas foram cadastradas')
#é possivel colocar listas dentro de listas, o código acima mostra o poder disso
