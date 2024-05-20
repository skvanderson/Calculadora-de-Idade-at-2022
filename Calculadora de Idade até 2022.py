from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = 2022
    idade = ano_atual - ano_nascimento
    return idade

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento entre 1922 a 2022 "))
            if 1922 <= ano_nascimento <= 2022:
                return ano_nascimento
            else:
                print("Por favor, digite um ano entre 1922 e 2022.")
        except ValueError:
            print("Por favor, digite um ano válido.")

def principal():
    nome_completo = input("Digite seu nome completo por favor ")
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)
    print(f"Olá, {nome_completo}!")
    if idade < 0:
        print("Você ainda não nasceu!")
    elif idade == 0:
        print("Você nasceu neste ano!")
    else:
        print(f"Você tem {idade} anos até o ano de 2022.")

if __name__ == "__main__":
    principal()

