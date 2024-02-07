import math

"""print("Bem vindo ao programa dos fatoriais.")

userinput=int(input("Introduza por favor um número."))

while userinput>=0:
    listfat=[]
    if userinput==0:
        resultado=math.prod(listfat)
        print(resultado)
    elif userinput>0:
        fato=(userinput-1)*userinput
        userinput=userinput-2
        listfat.append(fato)"""


print("Bem vindo ao programa dos fatoriais.")

num=int(input("Introduza por favor um número."))

c=num

f=1

while c>0:
    print(f"{c}", end="")
    print("x" if c> 1 else "=", end="")
    f *= c
    c -= 1
print(f"{f}")