from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.momento_cadastro.strftime('%d/%m/%Y %H:%M:%S')

    def mes(self):
        return self.momento_cadastro.strftime('%B')

    def dia_semana(self):
        return self.momento_cadastro.strftime('%A')
