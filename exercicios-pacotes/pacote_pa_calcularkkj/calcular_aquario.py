def procurando_volume(comprimento, altura, largura):
    return comprimento * altura * largura / 1000

def procurando_potencia(volume, temp_desejada, temp_atual):
    return volume * 0.05 * abs(temp_desejada-temp_atual)