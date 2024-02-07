import time

print("Bem vindo ao programa!")
time.sleep(1)
opt=0
while opt>=0:
    if opt==0:
        print("Introduza por favor três valores numéricos para os quais queira realizar operações.")
        num1= float(input("Introduza por favor o primeiro número: "))
        time.sleep(1)
        num2= float(input("Introduza por favor o segundo número: "))
        time.sleep(1)
        num3= float(input("Introduza por favor o terceiro número: "))
        time.sleep(1)
        opt= opt+1
    elif opt>0:
        opt=opt-1
        print("Escolha por favor uma das opções numéricas abaixo para prosseguir:\n[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA")

        opt=int(input("---->"))
        ordem=[]
        ordem.append(num1)
        ordem.append(num2)
        ordem.append(num3)
        if opt==1:
            print("A processar...")
            time.sleep(2)
            print(f"A soma dos números apresentados é {num1+num2+num3}")
        elif opt==2:
            print("A processar...")
            time.sleep(2)
            print(f"O produto dos números apresentados é {num1*num2*num3}")
        elif opt==3:
            print("A processar...")
            time.sleep(2)
            ordem.sort()
            print(f"A ordem ascendente dos números apresentados é {ordem}")
        elif opt==4:
            opt=opt-4
        elif opt==5:
            break
        else:
            print("Introduza por favor uma opção válida.")
