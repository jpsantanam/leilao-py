from arte import logo


def vencedorLeilao(apostas):
    vencedor = ""
    maiorAposta = 0

    for nome in apostas:
        apostaAtual = apostas[nome]
        if apostaAtual > maiorAposta:
            maiorAposta = apostaAtual
            vencedor = nome

    return f"O maior apostador foi {vencedor} com uma aposta de R${maiorAposta}."


def main():
    print(logo)

    vetorLeilao = {}
    deveContinuar = True

    while deveContinuar:
        nome = input("Qual é o seu nome? ")
        lance = float(input("Qual é o seu lance? R$"))
        vetorLeilao[nome] = lance
        deveContinuar = input("Há mais apostadores no leilão? ").lower() == "sim"
        print("")

    print(vencedorLeilao(vetorLeilao))


if __name__ == "__main__":
    main()
