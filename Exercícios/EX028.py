# EX028

cont1 = 0
cont2 = 0
cont3 = 0

while cont1 == 0:
    resposta1 = input("A pessoa que está a ler esta pergunta é linda. Verdadeiro ou falso (V/F)?").strip().lower()
    if resposta1 == 'v':
        print("Correto! Próxima pergunta.")
        cont1 += 1
    elif resposta1 == 'f':
        print("Tenha mais confiança na sua beleza. Próxima pergunta.")
        cont1 += 1
    else:
        print("Por favor introduza uma das opções apresentadas (V/F)")

while cont2 == 0:
    resposta2 = input("A pessoa que está a ler esta pergunta é inteligente. Verdadeiro ou falso (V/F)?").strip().lower()
    if resposta2 == 'v':
        print("Correto! Tal como uma pessoa inteligente diria!")
        cont2 += 1
    elif resposta2 == 'f':
        print("É mais inteligente do que parece, acredite. Vamos para a próxima.")
        cont2 += 1
    else:
        print("Por favor introduza uma das opções apresentadas (V/F)")

while cont3 == 0:
    resposta3 = input("A pessoa que está a ler esta pergunta é espetacular. Verdadeiro ou falso (V/F)?").strip().lower()
    if resposta3 == 'v':
        print("Correto! Ainda bem que estamos de acordo!")
        cont3 += 1
    elif resposta3 == 'f':
        print("Tenha mais confiança em si mesmo/a!")
        cont3 += 1
    else:
        print("Teimosia. Deves ser o César para estar com tanto sono. Por favor introduz uma das opções apresentadas, antes que me chateie! (V/F)")