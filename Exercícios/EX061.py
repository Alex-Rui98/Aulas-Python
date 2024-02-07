def recebe():
    num = int(input("Introduza um número:"))
    lista.append(num)


lista = list()
resp = "Y"
while resp == "Y":
    recebe()
    resp = input("Pretende continuar [Y/N]?")

print(max(lista))