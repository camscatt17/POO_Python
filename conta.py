class Conta():
    def __init__(self, numero, titular, saldo, limite): #Função que faz o papel de constutora no Python
        print("Construindo objeto {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O saldo {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor