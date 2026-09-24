
def analisar_cores(imagem):
    altura, largura, canais = imagem.shape

    media_canais = imagem.mean(axis=(0, 1))

    resultados = {
        "altura": altura,
        "largura": largura,
        "canais": canais,
        "valor_minimo": imagem.min(),
        "valor_maximo": imagem.max(),
        "media_geral": imagem.mean(),
        "media_azul": media_canais[0],
        "media_verde": media_canais[1],
        "media_vermelho": media_canais[2]
    }

    return resultados


def exibir_analise(resultados):
    print(f"Altura: {resultados['altura']} pixels")
    print(f"Largura: {resultados['largura']} pixels")
    print(f"Canais de cor: {resultados['canais']}")

    print(f"Valor mínimo: {resultados['valor_minimo']}")
    print(f"Valor máximo: {resultados['valor_maximo']}")
    print(f"Média geral: {resultados['media_geral']:.2f}")

    print(f"Média do azul: {resultados['media_azul']:.2f}")
    print(f"Média do verde: {resultados['media_verde']:.2f}")
    print(f"Média do vermelho: {resultados['media_vermelho']:.2f}")