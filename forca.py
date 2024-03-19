from random import choice

def convertor(a):
    b = []
    for x in a:
        b.append(x)
        return b
palavra = choice(["hitler","stalin","mao"])
palavra_mostrada = []
palavra_mostrada+= ["*"]*len(palavra)
tentativa = 3
for x in range(4):
    print(palavra_mostrada)
    palpite = input()
    for x,y in enumerate(palavra):
        if y == palpite:
            palavra_mostrada.pop(x)
            palavra_mostrada.insert(x,y)
        
    print("soubrou ",tentativa," tentativas")
    a = input("desejas sair? ")
    if a == "sim":
        break
    
