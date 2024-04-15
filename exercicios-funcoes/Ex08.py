from collections import Counter

def percorrerkkj(el_dicionario):
    for i in sorted(el_dicionario, key = lambda x:el_dicionario[x], reverse = True):
        print(f"{i} : {el_dicionario[i]} repetição(es)")

a = input("Digite uma frase:\n").lower().replace(",", " ").replace(".", " ").split()

a = Counter(a)

percorrerkkj(a)