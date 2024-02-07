dicio = {"Nome": "", "Media": "", "Situação": ""}

dicio["Nome"] = input("Introduza aqui o nome do aluno: ")
dicio["Media"] = float(input("Introduza aqui a média do aluno: "))
if dicio["Media"] >= 9.5:
    dicio["Situação"] = "Aprovado"
else:
    dicio["Situação"] = "Reprovado"

print(dicio)