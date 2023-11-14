from datetime import datetime
from Dispositivos.Dispositivo import Dispositivo
from random import randint

class SensorAgua(Dispositivo):
    """
    """

    def __init__(self, token : str, escala: str = "L", chanceOutlier: int = 5, nivelMaximo: int = 100) -> None:
        """
        """
        self.nivelMaximo = nivelMaximo
        self.chanceOutlier = chanceOutlier
        self.escala = escala
        self.nivelAtual = randint(0,nivelMaximo)
        self.timestampNivelAtual = datetime.now()
        super().__init__(token=token)
    
    def geraDados(self) -> dict:
        """
        """
        diferenca = randint(1, 5) + self.criaOutlier()
        nivelMedido = self.nivelAtual + diferenca
        timestampNivelMedido = datetime.now()
        if not self.outlier(nivelMedido=nivelMedido):
            self.nivelAtual = nivelMedido
            self.timestampNivelMedido = timestampNivelMedido
            return {
                'variable': 'Nível água',
                'value': self.temperaturaAtual, 
                'unit': self.escala, 
                'time': self.timestampTemperaturaAtual.strftime("%Y-%m-%d, %H:%M:%S")
            }
        else:
            raise Exception("Erro ao medir nivel!")
    
    def criaOutlier(self) -> int:
        """
        """
        chance = randint(0, 100)
        if chance <= self.chanceOutlier:
            return self.nivelMaximo+1
        else:
            return 0
        
    def outlier(self, nivelMedido: int) -> bool:
        """
        """
        if nivelMedido > self.nivelMaximo:
            return True
        else:
            return False