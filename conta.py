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
    
    def __pode_sacar(self, sacar_valor):
        valor_disponivel = self.__saldo + self.__limite
        return sacar_valor <= valor_disponivel
    
    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor passou o limite {valor}')
        
    def tranferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        
    @property   
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        
    