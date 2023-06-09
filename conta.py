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

    def __podeSacar(self, valor):
        return valor <= (self.__saldo + self.__limite)

    def saca(self, valor):
        if(self.__podeSacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapassou o limite da conta".format(valor))

    def transfere(self, valor,contaDestino):
        self.saca(valor)
        contaDestino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @property
    def conta(self):
        return self.__numero

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod #indica que o método é estático, ou seja refere-se à classe e não aos seus atributos
    def codigoBanco():
        return "001"

    @staticmethod
    def codigosBancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
