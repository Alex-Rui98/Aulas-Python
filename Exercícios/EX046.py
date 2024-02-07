listaprinc = []
listapar = []
listaimp = []
resp = "Y"

while resp == "Y":
    num = int(input("Introduza por favor um número:"))
    listaprinc.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimp.append(num)
    print("O número introduzido foi adicionado.")
    resp = input("Pretende continuar [Y/N]?")
    if resp == "N":
        print(listaprinc)
        print(listapar)
        print(listaimp)
        break
