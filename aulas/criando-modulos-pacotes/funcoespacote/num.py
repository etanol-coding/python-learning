def inputnumber(msg): #um input que só aceita números   
    while True:
        n = input(msg)
        if n.isnumeric():
            if float(n) == int(n):
                return int(n)
            else:
                return float(n)
        else:
            print('Digite em números, por favor!')
def tabuada(): #pergunta um número e printa sua tabuáda
    n = inputnumber('Digite um número:  ')
    for c in range(1, 10):
        print(f'{n} x {c} = {n*c}')