help(len) #retorna o funcionamente de uma função
print(print.__doc__) #printa a documentação da função
def somar(n1=0, n2=0, n3=0, n4=0, n5=0):
    #o comentário abaixo define o help da minha função
    """ 
    Soma até cinco números e retorna o resultado. 
    """
    return n1+n2+n3+n4+n5
help(somar)