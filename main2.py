import locale
from datas_br import DatasBr
from datetime import datetime, timedelta

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


momento_cadastro = DatasBr()
momento_agora = datetime.today()

print(momento_agora + timedelta(days=20))
print(momento_cadastro.mes().capitalize())
print(momento_cadastro.dia_semana().capitalize())
