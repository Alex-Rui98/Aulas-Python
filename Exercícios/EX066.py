def fatorial(num, mostrar=False):
    """

    :param num:
    :param mostrar:
    :return:
    """
    fat = 1
    for i in range(num, 0, -1):
        if mostrar:
            if i == 1:
                print(f"{i} = ", end ="")
            else:
                print(f"{i} x ", end="")
        fat *= i
    return fat



numero = int(input("Insira um número para ver o seu fatorial: "))
opcao = input("Deseja ver o processo? [S/N]\n--->").strip().lower()
mostrar = True if opcao == "s" else False
fatorial(numero, mostrar)
