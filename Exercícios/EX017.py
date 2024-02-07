#EX017

numero = int(input("Introduza um número inteiro:"))

print("[1]- Binário")
print("[2] - Octal")
print("[3] - Hexadecimal")

opcao=int(input("Digite a sua opção: "))

if opcao== 1:
    print(f"O número {numero} em binário é: {bin(numero)[2:]}")
elif opcao== 2:
    print(f"O número {numero} em Octal é: {oct(numero)[2:]}")
elif opcao== 3:
    print(f"O número {numero} em Hexadecimal é: {hex(numero)[2:]}")
else:
    print("A opção é inválida. Por favor tente novamente.")