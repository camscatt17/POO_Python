class Conta():
    def __init__(self, numero, titular, saldo, limite): #Função que faz o papel de constutora no Python
        print("Construindo objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor,contaDestino):
        self.saca(valor)
        contaDestino.deposita(valor)

    def getSaldo(self):
        return self.__saldo

    def getTitular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    def getNumeroConta(self):
        return self.__numero
    @limite.setter
    def limite(self, limite):
        self.__limite = limite