idade = int(input("Introduza aqui a sua idade"))
sexo = input("Introduza aqui a opcao que se adequa melhor ao seu genero [M/F/ND]").upper
cont25 = 0
cont17M = 0
contF = 0
contmenor = 0
resp = "Y"
while resp == "Y":
    if idade > 25:
        cont25 += 1
        resp = input("Deseja continuar [Y/N]")
        idade = int(input("Introduza aqui a sua idade"))
        sexo = input("Introduza aqui a opcao que se adequa melhor ao seu genero [M/F/ND]").upper
    elif idade < 17 and sexo == "M":
        cont17M += 1
        resp = input("Deseja continuar [Y/N]")
        idade = int(input("Introduza aqui a sua idade"))
        sexo = input("Introduza aqui a opcao que se adequa melhor ao seu genero [M/F/ND]").upper
    elif sexo == "F":
        contF += 1
        resp = input("Deseja continuar [Y/N]")
        idade = int(input("Introduza aqui a sua idade"))
        sexo = input("Introduza aqui a opcao que se adequa melhor ao seu genero [M/F/ND]").upper
    elif idade < 18:
        contmenor += 1
        resp = input("Deseja continuar [Y/N]")
        idade = int(input("Introduza aqui a sua idade"))
        sexo = input("Introduza aqui a opcao que se adequa melhor ao seu genero [M/F/ND]").upper
    elif resp == "N":
        print(f" Existem {cont25} pessoas com mais de 25 anos, {cont17M} homens com menos de 17 anos, {contF} mulheres e {contmenor} menores de idade.")