from datetime import datetime, time, timedelta
from Dispositivos.Dispositivo import Dispositivo
from random import randint

class SensorMovimento(Dispositivo):
    """
    """

    def __init__(self, token : str, horarioInicial: datetime.time = time(19, 00), diferencaTempoFinal: timedelta = timedelta(hours=2), chanceMovimento : int = 5) -> None:
        """
        """
        self.horarioInicial = horarioInicial
        self.diferencaTempoFinal = diferencaTempoFinal
        self.chanceMovimento = chanceMovimento
        super().__init__(token=token)
    
    def geraDados(self) -> dict:
        """
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
    
    def validaHorario(self):
        horarioAgora = datetime.now()
        horarioInicialHoje = datetime.combine(horarioAgora.date(), self.horarioInicial)
        horarioFinalHoje = horarioInicialHoje + self.diferencaTempoFinal
        if horarioAgora < horarioFinalHoje and horarioAgora > horarioInicialHoje:
            return True
        else: 
            return False