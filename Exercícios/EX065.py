from datetime import datetime

def validador_carta(ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    if idade>18:
        return f"Com {idade} anos, o cidadão pode tirar a carta de condução"
    elif idade <16:
        return f"Com {idade} anos, o cidadão não pode tirar a carta de condução"
    else:
        return f"Com {idade} anos, o cidadão pode tirar a carta de condução com autorização dos pais."


ano_nascimento = int(input("Digite o ano de nascimento do cidadão: "))
print(validador_carta(ano_nascimento))