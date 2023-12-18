class Conta: 
     
    def __init__(self, numero, titular, saldo, limite):
        print(f'Constuindo o Objeto {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print(f'Saldo de {self.__saldo}, do Titular {self.__titular}')
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor
        
    def tranferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)