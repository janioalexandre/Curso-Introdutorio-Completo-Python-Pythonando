notas = []

while True:
    nota = int(input("Digite uma nota (ou -1 para sair): "))
    if nota == -1:
        break
    notas.append(nota)

soma = 0
cont = 0
for i in notas:
    soma += i
    cont += 1
    
print(notas)
print(soma/cont)