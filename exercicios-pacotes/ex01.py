import pacote_pa_calcularkkj.calcular_aquario as nemo

comp = float(input("Digite o comprimento do aquário:\n"))
altu = float(input("Digite a altura do aquário:\n"))
largu = float(input("Digite a largura do aquário:\n"))

print("Agora, para calcularmos a potência necessária par ajustarmos o termostato, insira as informações a seguir")
temp_atual = float(input("Temperatura ambiente atual:\n"))
temp_desejada = float(input("Temperatura desejada:\n"))

vol = nemo.procurando_volume(comp, altu, largu)
pot = nemo.procurando_potencia(vol, temp_desejada, temp_atual)

print(f"Volume do aquário em litros: {vol:.2f} m³.")
print(f"A potência do termostato necessária para manter a temperatura adequada dentro do aquário: {pot:.2f} W.")
print(f"Para manter a qualidade da água, a quantidade de filtragem por hora deve ser de {vol*2:.2f} l/h a {vol*3:.2f} l/h.")