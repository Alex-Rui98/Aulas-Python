n= int(input("Introduza por favor a quantidade de números da sequência de Fibonacci que quer ver."))

a, b = 0, 1

count = 0
if n <= 0:
    print("Insira um número positivo")
elif n == 1:
    print("Sequência de Fibonacci até ao", n ,"termo:")
    print(a)
else:
    print ("Sequência de Fibonacci até ao", n ,"termo:")
    while count < n:
        print(a, end="~")
        fbs = a + b
        a = b
        b = fbs
        count += 1
print("FIM")