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
        self.valida_url_base()

    def valida_url_base(self):
        if not self.get_url_base().startswith("https://"):
            raise ValueError("URL inválida.")
        if not self.get_url_base().endswith("/cambio"):
            raise ValueError("Página não encontrada.")

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


#url = ExtratorURL("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
url= ExtratorURL(None)
valor_quantidade = url.get_valor_parametro("quantidade")
print(valor_quantidade)