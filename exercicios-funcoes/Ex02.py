def calc(v1,v2):
    return v1 * v2

a = int(input("Digite um número: "))

for i in range(1,11):
    print(f"{a} X {i} = {calc(a,i)}")