num = int(input("Introduza por favor um número para saber a sua tabuada:"))
cont = 0
res = None
while num > 0 and cont < 11:
    cont += 1
    res = num * cont
    print(f"{num} x {cont} = {res}")
    if cont==10:
        num = int(input("Introduza por favor um número para saber a sua tabuada:"))
        cont -= 10
    if num <= 0:
        break





