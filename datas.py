class datas:
    def data(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(f"Hoje é dia {self.dia:02d}/{self.mes:02d}/{self.ano}")