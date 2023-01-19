nota = float(input('Quanto você tirou na prova? '))
karma = 0
if nota == int(nota):
    nota = int(nota)
if nota>10: #nos if sempre utilize :
    print('O máximo era 10. Deixe de ser mentiroso') 
elif nota==10:
    print('O máximo era 10. Você com certeza colou, sua nota era 10. \n M A S  A G O R A  S E R A  Z E R O  S E U  I N C O M P E T E N T E')
elif nota >= 7: #else if é elif
    print(f'\nParabéns! a média era 7, Você tirou {nota} e passou!') #identação com TAB para criar um bloco
    karma == 1
else:
    print(f'\n A média era 7, Você tirou {nota}. \n M L K  B U R R O  I N C O M P E T E N T E')

n = 9.83753875873748374
print('passou de ano' if nota >=7 and nota <10  else f'te vejo ano que vem {n:.2f}')


