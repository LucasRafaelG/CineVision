
from pathlib import Path
import cv2

def carregar_imagem(caminho):
    imagem = cv2.imread(str(caminho))

    if imagem is None:
        raise FileNotFoundError(
            f"Não foi possível carregar a imagem: {caminho}"
        )

    return imagem