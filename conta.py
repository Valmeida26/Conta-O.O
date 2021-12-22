#classe

class Conta:

    def __init__(self, numero, titular, saldo, limite): #Atributos, o __init__ é o Construtor
        print(f"{titular}, seu número da conta é {numero}, seu saldo atual é {saldo} e seu limite é {limite}.")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo #torna privado o atributo saldo
        self.__limite = limite

    #metodos
    def extrato(self):
        print("Ola {}, seu saldo é R${}".format(self.__titular, self.__saldo))

    def deposita(self,valor):
        self.__saldo +=valor
        print(f"Ola {self.__titular}, você depositou R${valor} e seu saldo agora é de R${self.__saldo}")

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_saque

    #sacar
    def sacar(self,valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"Operação negada, você tentou sacar {valor}, mas seu limite é {self.__saldo + self.limite}")
         #   print(f"Ola {self.__titular}, você sacou R${valor} e seu saldo agora é de R${self.__saldo}")

    #transferir
    def transferir(self, valor, destino):
        self.sacar(valor)#O self faz o papel da origem(conta) ao transferir ex: conta.transferir(10,0 , conta2)
        destino.deposita(valor)
    #podemos criar getters e setters para acessar e alterar o valor de atributos privados

    #propiedades
    #saldo
    @property
    def saldo(self): #O GET é usado para retornar o valor , 'get' sempre tem um 'return'acompanhando
        return self.__saldo

    #titular
    def get_titular(self):
        return self.__titular

    #limite
    @property#è usada para acessar um conteúdo privado ex: self.__limite = limite
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self,limite):# O SET - "não devolve nada mas armazena o valor
        self.__limite = limite

    #Métodos estáticos
    @staticmethod
    def codigo_banco():
        return "001"
    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104"}
