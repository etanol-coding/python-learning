import funcoes #um modulo nada mais é que um arquivo.py com funções
nome = funcoes.inputword('Digite uma palavra: ')
print(f'{nome.capitalize().strip()} tem {len(nome)} caracteres.')
funcoes.ola() 
n1 = funcoes.inputnumber('Digite um número: ')
n2 = funcoes.inputnumber('Digite outro número: ')
print(f'A soma entre {n1} e {n2} resulta em {n1+n2}')
funcoes.tabuada() 
#os pacotes são conjuntos de modulos que podem ser divididos por categorias
from funcoespacote import num #modulo sobre numeros
from funcoespacote import string # modulo sobre strings
import funcoespacote # não da pra importar tudo, apesar de não dar erro, o que você importa são os modulos do pacoter não os pacotes em sí
