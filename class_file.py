class Conta: 
     
    def __init__(self, numero, titular, saldo, limite):
        print(f'Constuindo o Objeto {self}')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extrato(self):
        print(f'Saldo de {self.saldo}, do Titular {self.titular}')
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor