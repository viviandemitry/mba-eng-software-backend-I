import random

print('Boas vindas ao jogo do número secreto!\n')
numero_secreto = random.randint(1,5)
chute = int(input('Escolha um numero entre 1 e 5'))

if chute == numero_secreto:
    print('Voce acertou o numero secreto')
else:
    print(f'Quase.. O número secreto era {numero_secreto}')    