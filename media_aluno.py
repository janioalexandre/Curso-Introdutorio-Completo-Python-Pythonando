"""
    6 ou mais = Aprovado
    4 ou mais e menor do que 6 = Recuperação
    menos de 4 ele está de reprovação direta
"""

media = int(input("Digite a média do aluno: "))
taxa_de_presenca = int(input("Digite a taxa: "))

if media >= 6:
    print("Você foi aprovado.")
elif media >= 4:
    print("Você está de recuperação.")
else:
    print("Você foi reprovado.")