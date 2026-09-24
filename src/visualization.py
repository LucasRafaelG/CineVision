
import cv2
import matplotlib.pyplot as plt


def mostrar_histograma(imagem):
    azul, verde, vermelho = cv2.split(imagem)

    plt.hist(
        azul.ravel(),
        bins=256,
        range=(0, 256),
        color="blue",
        alpha=0.5,
        label="Azul"
    )

    plt.hist(
        verde.ravel(),
        bins=256,
        range=(0, 256),
        color="green",
        alpha=0.5,
        label="Verde"
    )

    plt.hist(
        vermelho.ravel(),
        bins=256,
        range=(0, 256),
        color="red",
        alpha=0.5,
        label="Vermelho"
    )

    plt.xlabel("Intensidade")
    plt.ylabel("Quantidade de pixels")
    plt.title("Distribuição dos canais de cor")
    plt.legend()
    plt.show()