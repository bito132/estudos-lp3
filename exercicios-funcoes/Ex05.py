def palindrometrokkj(a):
    return a == a[::-1]

a = input("Digite algo: ")

if(palindrometrokkj(a)):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")