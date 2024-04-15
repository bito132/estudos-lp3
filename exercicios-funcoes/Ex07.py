from random import randint

def enfocadora(word, letras):
    for i in letras:
        word = word.replace(i, "-")
    return word


palavras = ["bruxa", "vespa", "facada", "atletismo", "ecologista", "pneumoultramicroscopicossilicovulcanoconiotico", "loli", "naftalina", "torre", "teclado"]

palavra = palavras[randint(0,9)]
letras = set(palavra)

chances = len(letras) + 5


faiou = True
for i in range(chances, 0, -1):
    print(f"Chances restantes: {i}")
    a = input("Digite uma letra: ").lower()
    if(a in letras):
        letras.remove(a)
    print(enfocadora(palavra, letras))
    
    if(len(letras) == 0):
        print("Parábens, descobriu a palavra")
        faiou = False
        break

if(faiou):
    print(f"Boa tentativa, a palavra era {palavra}")