from datetime import datetime
from Dispositivos.Dispositivo import Dispositivo
from random import randint, uniform

class SensorUmidade(Dispositivo):
    """
    Simula um sensor de umidade.

    Herda da classe Dispositivo e representa um sensor de umidade que gera
    dados simulados de umidade em uma escala específica.

    Atributos
    ---------
        - chanceOutlier (int): A probabilidade de gerar um outlier.
            Padrão = 5%.
        - umidadeAtual (float): Última umidade medida pelo sensor.
        - timestampUmidadeAtual (datetime): O timestamp da última medição de umidade.
    """

    def __init__(self, token: str, chanceOutlier: int = 5) -> None:
        """
        Inicializador da classe do sensor de umidade.

        Parâmetros
        ----------
            - token (str): Token do dispositivo no TagoIO.
            - chanceOutlier (int): A probabilidade de gerar um outlier.
                Padrão = 5%.
        """
        self.chanceOutlier = chanceOutlier
        self.umidadeAtual = uniform(10, 90)
        self.timestampUmidadeAtual = datetime.now()
        super().__init__(token=token)
    
    def geraDados(self) -> dict:
        """
        Gera dados de umidade simulados.

        Retorna
        -------
            dict: Um dicionário contendo informações sobre a umidade gerada, incluindo
                'variable', 'value' e 'time'.
        
        Lança
        -----
            Exception: Se ocorrer um erro ao medir a umidade (quando há algum outlier).
        """
        diferenca = uniform(-2, 2) + self.criaOutlier()
        umidadeMedida = self.umidadeAtual + diferenca
        timestampUmidadeMedida = datetime.now()
        if not self.outlier(umidadeMedida=umidadeMedida):
            self.umidadeAtual = umidadeMedida
            self.timestampUmidadeAtual = timestampUmidadeMedida
            return {
                'variable': 'Umidade',
                'value': round(self.umidadeAtual, 2), 
                'time': self.timestampUmidadeAtual.strftime("%Y-%m-%d, %H:%M:%S")
            }
        else:
            raise Exception("Erro ao medir umidade!")
    
    def criaOutlier(self) -> int:
        """
        Gera um outlier com base na chance definida pelo sensor de umidade.

        Retorna
        -------
            int: Um valor de outlier (100) ou 0, dependendo da chance definida pelo sensor de umidade.
        """
        chance = randint(0, 100)
        if chance <= self.chanceOutlier:
            return 100
        else:
            return 0
        
    def outlier(self, umidadeMedida: float) -> bool:
        """
        Verifica se a umidade medida é um outlier. 

        Parâmetros
        ----------
            - umidadeMedida (float): A umidade medida a ser verificada.

        Retorna
        -------
            bool: True se for um outlier, False caso contrário.
                É considerado outlier quando a umidade medida é menor que 0 ou maior que 100.
        """
        if umidadeMedida < 0 or umidadeMedida > 100:
            self.umidadeAtual = uniform(10, 90)
            self.timestampUmidadeAtual = datetime.now()
            return True
        else:
            return False
