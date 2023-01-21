print('-' * 30) #utilize operadores aritimeticos para printar quantas vezes quiser um texto. 
input('Deseja saber sobre fatiamento de strings? Enter - Sim\n')
alfa = 'abcdefghijklmnopqrstuvwxyz'
print(f'String a fatiar: {alfa}')
print('\n\nSe você printar uma string como string[8] será printado o caractere 9, sendo o primeiro caractere o 0')
print(f'{alfa[7]} \n') #o oitavo caractere do alfabeto
print('O comando a seguir printa do 8º ao 10º caractere, sem contar o 10º ')
print(f'{alfa[7:9]}\n\n') #do oitavo ao decimo caractere do alfabeto
print('Se não colocar nada antes dos dois pontos : conta como primeiro caractere e depois dos dois pontos como ultimo.')
print(f'{alfa[:8]} \n{alfa[7:]}\n') #da primeira a 8 letra do alfabeto
print('Se colocar um terceiro número, vai pulando do número em número')
print(f'{alfa[4:13:2]}\n') #da 5 a 13 letra do alfabeto contando de 2 em 2
print(f'{alfa[6::2]} \n \n') #seguindo a mesma lógica, do g até o z pulando de 2 em 2
input('Deseja saber sobre analise de string? Enter - Sim\n')
ola = '  olá Tudo Bem Com Você?  '
print(f'String a analisar: {ola}')
print(f'{len(ola)}') #a função len() responde quantos caracteres efetivamente tem na variavel

olacount = ola.count('o', 0 , 8)
print(f'{olacount}\n')
    #a função count conta quantas vezes um caractere aparece na string. ou em uma parte da string, nesse caso indo do primeiro ao 7 caractere

olafind = ola.find('Com')
print(f'{olafind}\n')
    #o find indica em qual posição está uma serie de caracteres, se essa serie não existir, responderá -1

print('olá' in ola)
    #a mesma logica do find, porém ao inves de responde aonde está, responde se existe ou não com um resultado booleano

olareplace = ola.replace('olá ','oi, ')
print(f'{olareplace}\n')
    #o replace é bem simples, troca uma serie de caracteres(se ela existir) por outra

print(ola.upper())
    #transforma todos os caracteres em maiusculos

print(ola.lower())
    #transforma todos os caracteres em minusculos

print(ola.capitalize())
    #Transforma todos os caracteres em minusculos e somente o primeiro em maiusculo

print(ola.title())
    #transforma todo primeiro caractere de cada palavra em maisuculo

print(ola.strip())
    #retira todos os espaços do começo e do fim da string
print(ola.lstrip())
    #retira os espaços no começo da string
print(ola.rstrip())
    #retiras os espaços no fim da string

input('Você gostaria de saber sobre divisão e junção de strings? Enter - Sim\n\n')

vdd = 'tatch é uma boa lenda'
vddsplit = vdd.split()
print(f'{vddsplit} \n')
    #separa a string em palavras, em uma lista

print('-'.join(vddsplit))
    #junta a lista em uma string só, podendo selecionar o que separara as palavras novamente