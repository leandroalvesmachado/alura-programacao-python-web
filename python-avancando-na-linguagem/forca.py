def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "python"
    enforcou = False
    acertou = False

    # enquanto não enforcou e não acertou
    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip() # remove os espaços do inicio e do final
        index = 0

        for letra in palavra_secreta:
            # upper() = deixa as letras maiúsculas
            if (chute.upper() == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("jogando ...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
