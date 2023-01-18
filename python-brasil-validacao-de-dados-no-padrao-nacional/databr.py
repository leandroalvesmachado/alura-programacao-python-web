from datetime import datetime, timedelta # import para trabalhar com datas

class DataBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    # retorna o mês de cadastro baseado na variável momento_cadastro 
    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]

        mes_cadastro = self.momento_cadastro.month - 1
        
        return meses_do_ano[mes_cadastro]

    # retorna o dia da semana de cadastro baseado na variável momento_cadastro 
    def dia_semana(self):
        dia_semana_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]

        dia_semana = self.momento_cadastro.weekday()

        return dia_semana_lista[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        
        return data_formatada

    def tempo_cadastro(self):
        # agora = datetime.today() + timedelta(days=15, minutes=20,seconds=30)
        # return agora - self.tempo_cadastro
        tempo_cadastro = datetime.today() - self.momento_cadastro
        
        return tempo_cadastro