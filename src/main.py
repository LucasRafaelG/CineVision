
from pathlib import Path
import cv2

from image_loader import carregar_imagem
from color_analysis import analisar_cores, exibir_analise
from visualization import mostrar_histograma
from color_transform import aumentar_brilho


# ==========================================
# CONFIGURAÇÕES
# ==========================================

NOME_IMAGEM = "cabin2_scene_in_lake.png"

EXECUTAR_ANALISE = False
MOSTRAR_HISTOGRAMA = False
APLICAR_TRANSFORMACAO = True

INTENSIDADE_BRILHO = 30


# ==========================================
# EXECUÇÃO DO PROGRAMA
# ==========================================

def main():

    # Caminhos do projeto
    pasta_projeto = Path(__file__).parent.parent

    caminho_imagem = (
        pasta_projeto / "data" / "input" / NOME_IMAGEM
    )

    pasta_saida = pasta_projeto / "data" / "output"

    # Carregando a imagem
    imagem = carregar_imagem(caminho_imagem)

    print("Imagem carregada com sucesso!")

    # Análise de cores
    if EXECUTAR_ANALISE:
        resultados = analisar_cores(imagem)
        exibir_analise(resultados)

    # Histograma
    if MOSTRAR_HISTOGRAMA:
        mostrar_histograma(imagem)

    # Transformação de brilho
    if APLICAR_TRANSFORMACAO:

        imagem_clara = aumentar_brilho(
            imagem,
            intensidade=INTENSIDADE_BRILHO
        )

        # Criando a pasta de saída, caso não exista
        pasta_saida.mkdir(parents=True, exist_ok=True)

        caminho_saida = pasta_saida / "imagem_clara.jpg"

        sucesso = cv2.imwrite(str(caminho_saida), imagem_clara)

        if sucesso:
            print(f"Imagem transformada salva em: {caminho_saida}")
        else:
            print("Erro ao salvar a imagem transformada.")


if __name__ == "__main__":
    main()