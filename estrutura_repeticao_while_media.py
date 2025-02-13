soma = 0
nota = 0
cont = 0

while True:
    nota = int(input('Digite uma nota ou -1 para sair: '))
    if nota == -1:
        break

    soma = soma + nota
    cont = cont + 1

print(f'Foram digitadas {cont} notas')
print(f'A soma das notas é {soma}')
print(f'A média das notas é {soma / cont}')