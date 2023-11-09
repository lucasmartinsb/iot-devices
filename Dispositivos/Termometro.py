from datetime import datetime
from Dispositivos.Dispositivo import Dispositivo
from random import uniform, randint

class Termometro(Dispositivo):
    def __init__(self, escala : str = "C") -> None:
        token = "e5c937f2-164b-46a1-958c-a2eb2171d75c"
        self.temperaturaLimite = 50
        self.chanceOutlier = 5
        self.escala = escala 
        self.temperaturaAtual = uniform(18.0, 24.0)
        self.timestampTemperaturaAtual = datetime.now()
        super().__init__(token=token)
    
    def geraDados(self) -> dict:
        diferenca = uniform(0,1) + self.criaOutlier()
        temperaturaMedida = self.temperaturaAtual + diferenca
        timestampTemperaturaMedida = datetime.now()
        if not self.outlier(temperaturaMedida=temperaturaMedida, timestampTemperaturaMedida=timestampTemperaturaMedida):
            self.temperaturaAtual = round(temperaturaMedida, 2)
            self.timestampTemperaturaAtual = timestampTemperaturaMedida
            return {
                'variable' : 'Temperatura',
                'value' : self.temperaturaAtual, 
                'unit' : self.escala, 
                'time' : self.timestampTemperaturaAtual.strftime("%Y-%m-%d, %H:%M:%S")
            }
        else:
            raise Exception("Erro ao medir temperatura!")
    
    def criaOutlier(self) -> float:
        chance = randint(0,100)
        if chance <= self.chanceOutlier:
            return 100
        else:
            return 0
        
    def outlier(self, temperaturaMedida : float, timestampTemperaturaMedida : datetime) -> bool:
        if temperaturaMedida > self.temperaturaLimite:
            return True
        diferencaTemperatura = abs(self.temperaturaAtual - temperaturaMedida)
        diferencaTempo = (timestampTemperaturaMedida - self.timestampTemperaturaAtual).total_seconds()
        if diferencaTemperatura > diferencaTempo:
            return True
        else:
            return False