guarda = [[], []]

for i in range(0, 10):
    num = int(input(f"Introduza o {i+1}º número: "))
    if num % 2 == 0:
        guarda[0].append(num)
    else:
        guarda[1].append(num)

guarda[0].sort()
guarda[1].sort()

print(guarda)


