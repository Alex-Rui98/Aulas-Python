def msg():
    txt = input("Introduza o seu texto")
    fortxt = len(txt) * ".-"
    esp = " " * int(len(txt)/2)
    print(len(txt))
    print(f"-.-.-.-{fortxt}.-.-.-.-")
    print(f"       {esp}{txt}")
    print(f"-.-.-.-{fortxt}.-.-.-.-")

msg()