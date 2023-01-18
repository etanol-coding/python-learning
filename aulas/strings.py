input('Deseja saber sobre fatiamento de strings? Enter - Sim\n')
print('\n\nSe você printar uma string como string[8] será printado o caractere 9, sendo o primeiro caractere o 0')
alfa = 'abcdefghijklmnopqrstuvwxyz'
print(f'{alfa[7]} \n') #o oitavo caractere do alfabeto
print('O comando a seguir printa do 8º ao 10º caractere, sem contar o 10º ')
print(f'{alfa[7:9]}\n\n') #do oitavo ao decimo caractere do alfabeto
print('Se não colocar nada antes dos dois pontos : conta como primeiro caractere e depois dos dois pontos como ultimo.')
print(f'{alfa[:8]} \n{alfa[7:]}\n') #da primeira a 8 letra do alfabeto
print('Se colocar um terceiro número, vai pulando o número')
print(f'{alfa[4:13:2]}\n') #da 5 a 13 letra do alfabeto contando de 2 em 2
print(f'{alfa[6::2]} \n \n') #seguindo a mesma lógica, do g até o z pulando de 2 em 2
input('Deseja saber sobre analise de string? Enter - Sim\n')
ola = 'olá tudo bem com você?'
print(f'{len(ola)}') #a função len() responde quantos caracteres efetivamente tem na variavel
olacount = ola.count('o', 0 , 8)
#a função count conta quantas vezes um caractere apareceu na string. ou em uma parte da string, nesse caso indo do primeiro ao 7 caractere
print(f'{olacount}')

