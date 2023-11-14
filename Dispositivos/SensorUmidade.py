from datetime import datetime
from Dispositivos.Dispositivo import Dispositivo
from random import randint, uniform

class SensorUmidade(Dispositivo):
    """
    """

    def __init__(self, token: str, chanceOutlier: int = 5) -> None:
        """
        """
        self.chanceOutlier = chanceOutlier
        self.umidadeAtual = uniform(10, 90)
        self.timestampUmidadeAtual = datetime.now()
        super().__init__(token=token)
    
    def geraDados(self) -> dict:
        """
        """
        diferenca = uniform(-2, 2) + self.criaOutlier()
        umidadeMedida = self.umidadeAtual + diferenca
        timestampUmidadeMedida = datetime.now()
        if not self.outlier(umidadeMedida=umidadeMedida):
            self.umidadeMedida = umidadeMedida
            self.timestampUmidadeMedida = timestampUmidadeMedida
            return {
                'variable': 'Umidade',
                'value': self.umidadeMedida, 
                'time': self.timestampUmidadeAtual.strftime("%Y-%m-%d, %H:%M:%S")
            }
        else:
            raise Exception("Erro ao medir umidade!")
    
    def criaOutlier(self) -> int:
        """
        """
        chance = randint(0, 100)
        if chance <= self.chanceOutlier:
            return 100
        else:
            return 0
        
    def outlier(self, umidadeMedida: float) -> bool:
        """
        """
        if umidadeMedida < 0 or umidadeMedida > 100:
            self.umidadeAtual = 50
            return True
        else:
            return False
