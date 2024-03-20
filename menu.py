import c, forca
print("ola, bem vindo ao menu, escolha seu jogo: ")
print("forca e adivinhador de numeros")
a = input(" forca = f, e adivinhador de numeros = an: ")

if a == "an":
    c.adivinhacao()
elif a == "f":
    forca.Forca()