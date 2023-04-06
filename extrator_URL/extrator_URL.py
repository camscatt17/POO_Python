import re
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.index_separador_parametro = self.url.find("?")
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("URL inválida")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError('A URL não é válida')

    def get_url_base(self):
        return self.url[:self.index_separador_parametro]

    def get_url_parametro(self):
        return self.url[self.url.find("?")+1:]

    def get_valor_parametro(self, parametro):
        indice_parametro = self.get_url_parametro().find(parametro)
        indice_valor_parametro = indice_parametro+len(parametro)+1
        indice_divisor_parametro = self.get_url_parametro().find("&", indice_valor_parametro)
        if indice_divisor_parametro == -1:
            return self.get_url_parametro()[indice_valor_parametro:]
        else:
            return self.get_url_parametro()[indice_valor_parametro:indice_divisor_parametro]

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parêmetros: " + self.get_url_parametro()+ "\n" + "URL Bae: "+ self.get_url_base()
    def __eq__(self, other):
        return self.url == other.url

    def conversao(self):
        VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
        moeda_destino = self.get_valor_parametro("moedaDestino")
        quantidade = float(self.get_valor_parametro("quantidade"))
        if moeda_destino == 'dolar':
            print('O valor de {} dolares em reais é de:{}'.format(quantidade, round(VALOR_DOLAR * quantidade), 2))
        if moeda_destino == 'reais':
            print('O valor de {} reais em dolares é de:{}'.format(quantidade, round(VALOR_DOLAR/quantidade), 2))


url = ExtratorURL("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
print("O tamanho da URL: ", len(url))
print(url)
url.conversao()