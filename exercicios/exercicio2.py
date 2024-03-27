#Ex02 - Escreva um programa em Python que solicita ao usuário três números e apresenta a média aritmética dos números informados.
a,b,c = [float(x) for x in input("Digite 3 números com um espaço entre eles: ").split(" ")]
print(f"Média com 2 casas decimais de aproximação: {(a+b+c)/3:.2f}")