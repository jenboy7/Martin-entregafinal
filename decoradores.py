def deco(func):
    def contenedor(a,b):
        print('Print de deco')
        func(a,b)
        print('Otro de deco')
    return contenedor

@deco
def suma(a, b):
    return a+b

suma(1,2)


print(suma(2,2))