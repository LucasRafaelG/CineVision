
def aumentar_brilho(imagem, intensidade=30):
    imagem_int = imagem.astype("int16")

    imagem_clara = imagem_int + intensidade

    imagem_clara = imagem_clara.clip(0, 255).astype("uint8")

    return imagem_clara