from random import choice
def Forca():
    def print_convert(a):
        b = ''.join(a)
        return b
    def convertor(a):
        b = []
        for x in a:
            b.append(x)
            return b
    palavra = choice(["hitler","stalin","mao","frutas"])
    palavra_mostrada = []
    palavra_mostrada+= ["*"]*len(palavra)
    tentativa = len(palavra)+2
    tentativa_mostrada = tentativa
    for i in range(tentativa):
        print(print_convert(palavra_mostrada))
        
        palpite = input()
        for x,y in enumerate(palavra):
            if y == palpite:
                palavra_mostrada.pop(x)
                palavra_mostrada.insert(x,y)
        tentativa_mostrada-=1
        if print_convert(palavra_mostrada) == print_convert(palavra):
            print(print_convert(palavra_mostrada))
            print("você ganhou")
            break
        else:
            print("soubrou ",tentativa_mostrada," tentativas")
