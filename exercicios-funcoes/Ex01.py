from random import randint

def adivinha(val, target):
    return val == target

target = randint(1, 100)

while(True):
    a = int(input("Tente adivinhar o número: "))

    if(adivinha(a, target)):
        print("Acertou!")
        break
    elif(a < target):
        print("Palpite abaixo do número alvo")
    else:
        print("Palpite acima do número alvo")