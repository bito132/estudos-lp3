#Ex03 - Crie um programa em Python que recebe como entrada o valor de uma compra e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:

#    Compras entre R$ 0,01 e R$ 9,99 - 0% de desconto
#    Compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
#    Compras entre R$ 100,00 e R$ 499,99 - 10% de desconto
#    Compras iguais ou superiores a R$ 500,00 - 15% de desconto
a = float(input())

if(a >= 0.01 and a <= 9.99):
    d = 0
    print(f"valor final da compra: R$ {a - a*d:.2f}")  
elif(a < 100):
    d = 0.05
    print(f"valor final da compra: R$ {a - a*d:.2f}")
elif(a < 500):
    d = 0.1
    print(f"valor final da compra: R$ {a - a*d:.2f}")
else:
    d = 0.15
    print(f"valor final da compra: R$ {a - a*d:.2f}")