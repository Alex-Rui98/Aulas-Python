#EX025

frase = input("Introduza aqui o seu possível palíndromo:").strip().upper()

palavras = frase.split()
juntas = "".join(palavras)
inverso= juntas[::-1]

if juntas == inverso:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")

print(juntas)
print(inverso)