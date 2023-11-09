from datetime import datetime
from Dispositivos.Dispositivo import Dispositivo
from random import uniform, randint

class Termometro(Dispositivo):
    """
    Simula um termômetro digital.

    Herda da classe Dispositivo e representa um termômetro que gera
    dados de temperatura em uma escala específica.

    Atributos
    ---------
        - escala (str): A escala de temperatura utilizada
            Padrão = Celsius ("C")
        - chanceOutlier (int): A probabilidade de gerar um outlier
            Padrão = 5%.
        - temperaturaLimite (int): A temperatura limite para considerar um outlier
            Padrão = 50.
        - temperaturaAtual (float): Última temperatura marcada pelo termômetro.
        - timestampTemperaturaAtual (datetime): O timestamp da última medição de temperatura.
    """

    def __init__(self, token : str, escala: str = "C", chanceOutlier: int = 5, temperaturaLimite: int = 50) -> None:
        """
        Inicializador da classe de termômetro.

        Parâmetros
        ----------
            - token (str): Token do dispositivo no TagoIO
            - escala (str): A escala de temperatura utilizada
                Padrão = Celsius ("C")
            - chanceOutlier (int): A probabilidade de gerar um outlier
                Padrão = 5%.
            - temperaturaLimite (int): A temperatura limite para considerar um outlier
                Padrão = 50.
        """
        self.temperaturaLimite = temperaturaLimite
        self.chanceOutlier = chanceOutlier
        self.escala = escala 
        if escala == "C":
            self.temperaturaAtual = uniform(18.0, 24.0)
        elif escala == "F":
            self.temperaturaAtual = uniform(64, 75)
        self.timestampTemperaturaAtual = datetime.now()
        super().__init__(token=token)
    
    def geraDados(self) -> dict:
        """
        Gera dados de temperatura simulados.

        Retorna
        -------
            dict: Um dicionário contendo informações sobre a temperatura gerada, incluindo
                'variable', 'value', 'unit' e 'time'.
        
        Lança
        -----
            Exception: Se ocorrer um erro ao medir a temperatura (quando há algum outlier).
        """
        diferenca = uniform(0, 1) + self.criaOutlier()
        temperaturaMedida = self.temperaturaAtual + diferenca
        timestampTemperaturaMedida = datetime.now()
        if not self.outlier(temperaturaMedida=temperaturaMedida, timestampTemperaturaMedida=timestampTemperaturaMedida):
            self.temperaturaAtual = temperaturaMedida
            self.timestampTemperaturaAtual = timestampTemperaturaMedida
            return {
                'variable': 'Temperatura',
                'value': round(self.temperaturaAtual, 2), 
                'unit': self.escala, 
                'time': self.timestampTemperaturaAtual.strftime("%Y-%m-%d, %H:%M:%S")
            }
        else:
            raise Exception("Erro ao medir temperatura!")
    
    def criaOutlier(self) -> float:
        """
        Gera um outlier com base na chance definida pelo termômetro.

        Retorna
        -------
            float: Um valor de outlier (100) ou 0, dependendo da chance definida pelo termômetro.
        """
        chance = randint(0, 100)
        if chance <= self.chanceOutlier:
            return 100
        else:
            return 0
        
    def outlier(self, temperaturaMedida: float, timestampTemperaturaMedida: datetime) -> bool:
        """
        Verifica se a temperatura medida é um outlier. 
        A verificação é baseada na temperaturaLimite e diferença entre a última temperatura medida.

        Parâmetros
        ----------
            - temperaturaMedida (float): A temperatura medida a ser verificada.
            - timestampTemperaturaMedida (datetime): O timestamp da medição de temperatura.

        Retorna
        -------
            bool: True se for um outlier, False caso contrário.
                É considerado outlier quando a temperatura medida é maior que a temperatura limite do termômetro
                ou quando a diferença de temperatura entre a medição atual e anterior é maior que a diferença de tempo em segundos.
        """
        if temperaturaMedida > self.temperaturaLimite:
            return True
        diferencaTemperatura = abs(self.temperaturaAtual - temperaturaMedida)
        diferencaTempo = (timestampTemperaturaMedida - self.timestampTemperaturaAtual).total_seconds()
        if diferencaTemperatura > diferencaTempo:
            return True
        else:
            return False