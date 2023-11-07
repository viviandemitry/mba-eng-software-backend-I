def oi():
    print('oi')

oi() #chama a funcao

def soma():
    print(40+2)

soma()

def soma_com_argumentos(a, b):
    print(a + b)

soma_com_argumentos(5, 6) 

def soma_com_argumentos(a, b):
    return a + b

resposta = soma_com_argumentos(5, 6) 
print(resposta)