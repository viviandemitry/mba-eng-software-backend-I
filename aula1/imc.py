print('IMC\n')

# peso / altura * altura

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / altura ** 2
imc = round(imc, 2) 

print(f'\n O IMC e {imc}')