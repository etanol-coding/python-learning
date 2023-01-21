def teste(parametro):
    print(parametro)
    var = 2 #no escopo dessa função foi criada uma nova variavel chamada var, nada foi redefinido
    print(var)
    import random
    print(random.randrange(1, 10)) #o modulo random é importado apenas para o escopo dessa função
var = 1 #no escopo global foi criado a nova variavel chamada var
teste(var)
print(var)
print('\n\nErro:\n\n\n')
print(random.randrange(1, 10)) #isso dará erro pois no escopo global o modulo random não foi importado