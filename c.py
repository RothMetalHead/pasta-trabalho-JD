import random
dificuldade = input("escolha a dificuldade facil,normal,dificil,impossivel: ")

if dificuldade == "facil":
    mensagem = "escolha um numero de 0 a 5: "
    numero = random.randrange(0,5)
    chances = 9
elif dificuldade == "normal":
    mensagem = "escolha um numero de 0 a 10: "
    numero = random.randrange(0,10)
    chances = 6
elif dificuldade == "dificil":
    mensagem = "escolha um numero de 0 a 25: "
    numero = random.randrange(0,25)
    chances = 4
elif dificuldade == "impossivel":
    mensagem = "escolha um numero de 0 a 50: "
    numero = random.randrange(0,50)
    chances = 3


for x in range(chances):
    palpite = int(input(mensagem))
    a = 0
    if palpite == numero:
        print("ganhou, outro numero foi sorteado, e uma nova chance foi colocada")
        numero = random.randrange(0,10)
        chances+=1
    elif palpite > numero:
        print("o numero é menor")
        chances-=1
    elif palpite < numero:
        print("o numero é maior")
        chances-=1

    if chances == 1 and numero > 10:
        numero_string = str(numero)
        
        print("o numero termina com: ",x)

        print("DICA: o numero é maior")
        chances-=1
        

        
if chances == 0:

    print("perdeu, o numero era: ",numero)
    print(x)

