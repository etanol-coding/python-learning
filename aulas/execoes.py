try:
    n = int(input('digite um número: '))
    print(3/n) #execões são erros sem ser um erro de sintaxe
except ZeroDivisionError:
    print('você tentou dividir por 0')
except Exception as erro:
    print(f'erro encontrado:  {erro.__class__}')
else:
    print('Nenhum erro ocorreu')
finally:
    print('volte sempre')