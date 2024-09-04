nota1 = float(input("Digite a nota da atividade 1 : "))
nota2 = float(input("Digite a nota da ativadade 2 : "))
nota3 = float(input("Digite a nota da ativadade 3: "))
nota4 = float(input("Digite a nota da ativadade 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7.5:
    print("Passou de ano tranquilo, com média: %.1f"%media)
elif media >= 5:
    print("Passou de ano, mas no sufuco - com média: %.1f"%media)
else:
    print("Reprovou no bimestre, com média: %.1f"%media)