#Não achei nenhuma forma padrão de converter as notas, então fiz desse jeito

def conversor(val):
    if(val == 100):
        return "A"
    elif(val > 79):
        return "B"
    elif(val > 69):
        return "C"
    elif(val > 59):
        return "D"
    else:
        return "F"
    
a = int(input("Digite sua nota: "))
print(f"Sua nota equivale a uma nota {conversor(a)}")
