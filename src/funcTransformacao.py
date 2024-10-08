import classObjGeometricos as obj

#transforma um ponto
def transformar_ponto(coordenada, window, viewport):
    xwmin, ywmin = window[0].x, window[0].y
    xwmax, ywmax = window[1].x, window[1].y
    xvmin, yvmin = viewport[0].x, viewport[0].y
    xvmax, yvmax = viewport[1].x, viewport[1].y

    xv = xvmin + (coordenada.x - xwmin) * (xvmax - xvmin) / (xwmax - xwmin)
    yv = yvmin + (coordenada.y - ywmin) * (yvmax - yvmin) / (ywmax - ywmin)

    return obj.Ponto(xv, yv)

# Função para transformar as coordenadas dos objetos para o sistema de coordenadas da viewport
# não aplica margem
# não inverte o y
def transformar(window, viewport, pontos, retas, poligono):
    viewport_x = int(viewport[1].x) - int(viewport[0].x)
    viewport_y = int(viewport[1].y) - int(viewport[0].y)

    window_x = int(window[1].x) - int(window[0].x)
    window_y = int(window[1].y) - int(window[0].y)

    largura = viewport_x / window_x
    altura = viewport_y / window_y

    # Aplicando a transformação nos pontos
    for ponto in pontos:
        ponto.x = int(ponto.x) * largura
        ponto.y = int(ponto.y) * altura

    # Aplicando a transformação nas retas
    for reta in retas:
        reta.ponto1.x = int(reta.ponto1.x) * largura
        reta.ponto2.x = int(reta.ponto2.x) * largura
        reta.ponto1.y = int(reta.ponto1.y) * altura
        reta.ponto2.y = int(reta.ponto2.y) * altura

    # Aplicando a transformação no polígono
    for ponto in poligono:
        ponto.x = int(ponto.x) * largura
        ponto.y = int(ponto.y) * altura

    # Atualizando os limites da window para os da viewport
    window[0].x = 0
    window[0].y = 0
    window[1].x = viewport_x
    window[1].y = viewport_y

#função para transformar os pontos para o sistema de coordenadas da viewport com a margem e o y invertido
def transformar2(pontos,retas,poligonos,window,viewport):
    viewport_x = float(viewport[1].x) - float(viewport[0].x)
    viewport_y = float(viewport[1].y) - float(viewport[0].y)

    window_x = float(window[1].x) - float(window[0].x)
    window_y = float(window[1].y) - float(window[0].y)

    largura = viewport_x / window_x
    altura = viewport_y / window_y

    margem_y = float(viewport[0].y)
    margem_x = float(viewport[0].x)

    # Aplicando a transformação nos pontos
    for ponto in pontos:
        ponto.x = (float(ponto.x) * largura) + margem_x
        ponto.y = float(viewport_y) - ((float(ponto.y) * altura)) + margem_y

    # Aplicando a transformação nas retas
    for reta in retas:
        reta.ponto1.x = (float(reta.ponto1.x) * largura) + margem_x
        reta.ponto2.x = (float(reta.ponto2.x) * largura) + margem_x
        reta.ponto1.y = float(viewport_y) - ((float(reta.ponto1.y) * altura)) + margem_y
        reta.ponto2.y = float(viewport_y) - ((float(reta.ponto2.y) * altura)) + margem_y

    # Aplicando a transformação no polígono
    for poligono in poligonos:

        for ponto in poligono.pontos:
            ponto.x = (float(ponto.x) * largura) + margem_x
            ponto.y = float(viewport_y) - ((float(ponto.y) * altura)) + margem_y

    # Atualizando os limites da window para os da viewport
    window[0].x = 0
    window[0].y = 0
    window[1].x = viewport_x + margem_x
    window[1].y = viewport_y + margem_y
