#EX018

num1=int(input("Introduza um número: ").strip())

num2=int(input("Introduza outro número: ").strip())

if num1>num2:
    print(f"O número {num1} é maior que {num2}")
elif num1<num2:
    print(f"O número {num1} é menor que {num2}")
elif num1==num2:
    print("Os números são iguais!")