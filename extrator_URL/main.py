url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

#Separa base e parâmetros
url_base = url[0:url.find('?')]
print(f'URL base: {url_base}')

url_parametros = url[url.find('?')+1:]
print(f'URL parametros: {url_parametros}')


#Busca valor de um parâmetro
parametro_busca ='quantidade'
indice_parametro=url_parametros.find(parametro_busca)
indice_valor_parametro= indice_parametro+len(parametro_busca)+1
indice_divisor_parametros = url_parametros.find('&', indice_valor_parametro)

if indice_divisor_parametros == -1:
    valor = url_parametros[indice_valor_parametro:]
else:
    valor = url_parametros[indice_valor_parametro:indice_divisor_parametros]

print(valor)

