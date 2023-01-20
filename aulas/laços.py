'''for c in range(1,6): #defina quantas vezes ira se repetir+1
    print(c)
    if c == 5:  #coloque ifs dentro de laços!
        print('fim')'''
c = 'S'
while c =='S': #apeneas defina uma condição, não nescessáriamente quantas vezes irá se repetir
    print('O Naruto pode ser um pouco duro as vezes, talvez você não saiba disso, mas o Naruto também cresceu sem pai. Na verdade ele nunca conheceu nenhum de seus pais, e nunca teve nenhum amigo em nossa aldeia. Mesmo assim eu nunca vi ele chorar, ficar zangado ou se dar por vencido, ele está sempre disposto a melhorar, ele quer ser respeitado, é o sonho dele e o Naruto daria a vida por isso sem hesitar. Meu palpite é que ele se cansou de chorar e decidiu fazer alguma coisa a respeito! \n')
    repetir = str(input('Deseja repetir? S/N  ').upper())
    if repetir == 'N':
        break #O comando break para a repetição e volta ao código normal
print('cógido normal')

