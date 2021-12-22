class cliente:
    def __init__(self, nome):
        self.__nome = nome

        @property #è um decorador (GETTER) serve para ler um atributo
        def nome(self):
            print("Chamando @property nome...")
            return self.__nome.title()
        @nome.setter #SETTER serve para acessar um atributo e deve ser usado com o getter
        def nome(self):
            print("Chamando setter nome...")
            self.__nome = nome







