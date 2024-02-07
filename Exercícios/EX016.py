#EX016

nota= input("Introduza as notas do aluno, separadas apenas por um espaço:").strip()

contador= nota.count(" ") + 1

print(contador)

nota_sep=nota.split(" ")

media= (float(nota_sep[0])+ float(nota_sep[1])+ float(nota_sep[2])+ float(nota_sep[3])+ float(nota_sep[4]))/contador

print(media)

if (media<8):
    print("Infelizmente reprovou,com uma média de", media )
elif (media<9.5):
    print("Prepare-se para a recuperação, com uma média de", media)
else:
    print("Parabéns, passou com uma média de", media)