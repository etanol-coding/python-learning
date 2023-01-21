import emoji #importa o pacote por inteiro, mais recomendado
from random import randint, choice #importa funções especificas
print('\n\nMódulos são funções a mais ao python\n')
print('Importe um módulo no começo do código com import (nome do módulo) \n importe apenas as funções que você precisa com from (nome do modulo) import (função desejada) \n')
print('Além dos módulos préinstalados do python, existem os criados por usuários. \nEsses você acessa pelo python.org na aba PyPi, apenas selecione o módulo, e cole seu código no prompt do windows. \nGeralmente as intruções e funcionalidades estarão na página do módulo. \n')
print(emoji.emojize(f'Python é {randint(1, 10)}/10  :thumbsup: \n\n', language='alias'))
lista = [1, 2, 'não']
print(choice(lista))