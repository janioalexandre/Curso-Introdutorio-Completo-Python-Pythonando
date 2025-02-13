pessoas = []

while True:
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    
    if idade == -1:
        break

    dicionario = {"nome": nome, "idade": idade}
    pessoas.append(dicionario)

print(pessoas)
