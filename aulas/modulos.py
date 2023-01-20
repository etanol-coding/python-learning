import emoji
import random
print('\n\nMódulos são adições ao python, como o random que permite sortear um valor de uma lista, ou o math que adiciona novas funções de matemática \n')
print('Importe um módulo no começo do código com import (nome do módulo) \n importe apenas as funções que você precisa com from (nome do modulo) import (função desejada) \n')
print('Além dos módulos préinstalados do python, existem os criados por usuários. \nEsses você acessa pelo python.org na aba PyPi, apenas selecione o módulo, e cole seu código no prompt do windows. \nGeralmente as intruções e funcionalidades estarão na página do módulo. \n')
print(emoji.emojize(f'Python é {random.randint(1, 10)}/10  :thumbsup: \n\n', language='alias'))
lista = [1, 2, 'não']
print(random.choice(lista))