dicionario = {
    'nome':'daniel',
    'idade': 12
    } #definido por {}    troca o indice por chaves como 'daniel' ou 'idade'
print(dicionario['nome'])
dicionario = dict() #ou por dict()
dicionario['dado chato'] = "A barragem da maior usina hidrelétrica do mundo, a Usina das Três Gargantas, localizada na China, prolongaria a duração do dia em 0,66 microssegundos se operasse em sua capacidade máxima. Isso ocorreria em virtude da enorme massa de água que ela comporta."
#cria um item 
print(dicionario)
dicionario['dado chato'] = "O cachorro-quente é uma invenção alemã do século XV." #reatribui um valor
print(dicionario)
del dicionario['dado chato'] #exclui o item
dicionario = {
    'nome':'Daniel Rizato',
    'idade':'12',
    'sexo':'masculino',
}
print(dicionario.keys()) #equivale as chaves do dicionário
print(dicionario.values()) #equivale aos valores do dicionário
print(dicionario.items()) #equivale aos items do dicionário
for v,k in dicionario.items():
    print(f'Seu {v} é {k}.')
