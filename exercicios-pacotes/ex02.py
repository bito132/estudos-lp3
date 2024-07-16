from pacote_pa_calcularkkj.calcular_IMC import imc

peso = float(input("Digite o seu peso:\n"))
altu = float(input("Digite a sua altura:\n"))

imc = imc(peso, altu)
vai_ter_que_calcular = True

if(imc < 18.5):
    print("Você está abaixo do peso ideal.")
elif(imc < 25):
    print("Você está no peso ideal.")
    vai_ter_que_calcular = False
elif(imc < 30):
    print("Você com excesso de peso.")
elif(imc < 35):
    print("Você com obesidade de classe 1.")
elif(imc < 40):
    print("Você com obesidade de classe 2.")
else:
    print("Você com obesidade de classe 3.")

if(vai_ter_que_calcular):
    print(f"Você precisa perder {imc - 24.9:.3f} Kg para estar no peso ideal.") if imc > 24.9 else print(f"Você precisa ganhar {18.5 - imc:.3f} Kg para estar no peso ideal.")