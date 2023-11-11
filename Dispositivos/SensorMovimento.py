from datetime import datetime, time, timedelta
from Dispositivos.Dispositivo import Dispositivo
from random import randint

class SensorMovimento(Dispositivo):
    """
    Simula um sensor de movimento.

    Herda da classe Dispositivo e representa um sensor de movimento que gera
    dados simulados de movimentação com base em horários e probabilidades específicas.

    Atributos
    ---------
        - horarioInicial (datetime.time): O horário inicial para considerar a possibilidade de movimento.
            Padrão = 19:00 (7:00 PM).
        - diferencaTempoFinal (timedelta): O intervalo de tempo durante o qual o movimento é possível.
            Padrão = 2 horas.
        - chanceMovimento (int): A probabilidade de detectar movimento.
            Padrão = 5%.
    """

    def __init__(self, token: str, horarioInicial: datetime.time = time(19, 00), diferencaTempoFinal: timedelta = timedelta(hours=2), chanceMovimento: int = 5) -> None:
        """
        Inicializador da classe do sensor de movimento.

        Parâmetros
        ----------
            - token (str): Token do dispositivo no TagoIO
            - horarioInicial (datetime.time): O horário inicial que define se vai enviar ou não o movimento.
                Padrão = 19:00 (7:00 PM).
            - diferencaTempoFinal (timedelta): O intervalo de tempo par adefinir o horário final para considerar ou não o movimento.
                Padrão = 2 horas.
            - chanceMovimento (int): A probabilidade de detectar movimento.
                Padrão = 5%.
        """
        self.horarioInicial = horarioInicial
        self.diferencaTempoFinal = diferencaTempoFinal
        self.chanceMovimento = chanceMovimento
        super().__init__(token=token)
    
    def geraDados(self) -> dict:
        """
        Gera dados simulados de movimento.

        Retorna
        -------
            dict: Um dicionário contendo informações sobre a detecção de movimento, incluindo
                'variable', 'value' e 'time'. Retorna None se não houver movimento detectado.
        """
        chance = randint(0, 100)
        if chance <= self.chanceMovimento and self.validaHorario():
            return {
                'variable': 'Movimento',
                'value': 'Movimentação',
                'time': datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
            }
        else:
            return None
    
    def validaHorario(self) -> bool:
        """
        Verifica se o horário atual está dentro do intervalo de tempo definido para detectar movimento.

        Retorna
        -------
            bool: True se estiver dentro do horário definido, False caso contrário.
        """
        horarioAgora = datetime.now()
        horarioInicialHoje = datetime.combine(horarioAgora.date(), self.horarioInicial)
        horarioFinalHoje = horarioInicialHoje + self.diferencaTempoFinal
        if horarioAgora < horarioFinalHoje and horarioAgora > horarioInicialHoje:
            return True
        else: 
            return False