def calcVolume(comprimento, altura, largura):

    return comprimento*altura*largura/1000

def calcPotencia(volume, tempDesejada, tempAmbiente):

    return volume * 0.05 * (tempDesejada - tempAmbiente)