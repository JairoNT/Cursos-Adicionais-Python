from datetime import datetime, timedelta


class DatasBR:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%y %H:%M")
        return data_formatada

    def mes_cadastro(self):
        meses_do_ano = [
            "Janeiro", "Fevereiro", "Março",
            "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro",
            "Outubro", "Novembro", "Dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month -1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def tempo_de_cadastro(self):
        tempo_de_cadastro = datetime.today() - self.momento_cadastro
        return tempo_de_cadastro
