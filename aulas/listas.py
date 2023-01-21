lista = [
    'item1',
    'item2',   # listas são definidas por []
    'item3'
         ]
#indices indice0  indice1  indice2
if 'item1' in lista: #testa se existe um item na lista
    print(lista)
print(lista[0:3:2])
print(len(lista)) #responde quantos items tem na lista
lista[2] = 'amogus' #listas são mutáveis
lista.append('item4') #adiciona um item a lista
print(len(lista))
lista.insert(1, 'insertado') #adiciona um item no indice de um valor
print(lista)
del lista[4]
lista.pop() #elimina o último item
lista.pop(0) #também pode escolher qual eliminar
lista.remove('item2') #elimina um item em especifico
print(lista)
lista = list(range(1, 4)) #crie uma lista com o list() e o range()
lista = list(3, 6, 9) #ou sem o range...
lista[2] = int(input('digite um número --->  '))
lista.sort() #coloca os números da lista em ordem crescente ou alfabetica
print(lista)
lista.sort(reverse=True) #coloca os valores da lista em ordem decrescente ou o contrário do alfabeto
print(lista)
listafor = list()
print(len(lista))
for c in range(0, 3):
    listafor.append(input('digite algo --->  '))
print(listafor)
listafor.clear() #.clear() exclui todos os itens da lista
print(listafor)
