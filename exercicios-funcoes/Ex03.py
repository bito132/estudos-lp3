#só taquei o código embaixo pq era mais fácil pra resolver
#for i in range(97,123):
#    print(f'''"{chr(i)}", ''', end = '')

def calc_vogal(a):
    r = 0
    for i in ["a", "e", "i", "o", "u"]:
        r += a.count(i)
    return r

def calc_consoante(a):
    r = 0
    for i in ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]:
        r += a.count(i)
    return r

a = input("Digite uma frase:\n").lower()

print(f"Nesta frase há {calc_vogal(a)} vogais e {calc_consoante(a)} consoantes.")