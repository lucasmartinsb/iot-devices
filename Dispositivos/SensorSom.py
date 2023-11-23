from datetime import datetime
from Dispositivos.Dispositivo import Dispositivo
from random import randint, uniform


class SensorSom(Dispositivo):
    """
    Simula um sensor de nível de som.

    Herda da classe Dispositivo e representa um sensor de som que gera
    dados simulados de som em uma escala específica.

    Atributos
    ---------
        - chanceOutlier (int): A probabilidade de gerar um outlier.
            Padrão = 5%.
        - somAtual (float): Último som medido pelo sensor.
        - timestampsomAtual (datetime): O timestamp da última medição de som.
    """

    def __init__(self, token: str,  escala: str = "d",chanceOutlier: int = 5) -> None:
        """
        Inicializador da classe do sensor de som.

        Parâmetros
        ----------
            - token (str): Token do dispositivo no TagoIO.
            - chanceOutlier (int): A probabilidade de gerar um outlier.
                Padrão = 5%.
        """
        self.chanceOutlier = chanceOutlier
        self.somAtual = uniform(10, 90)
        self.escala = escala
        self.timestampsomAtual = datetime.now()
        super().__init__(token=token)

    def geraDados(self) -> dict:
        """
        Gera dados de som simulados.

        Retorna
        -------
            dict: Um dicionário contendo informações sobre o som gerado, incluindo
                'variable', 'value' e 'time'.

        Lança
        -----
            Exception: Se ocorrer um erro ao medir o som (quando há algum outlier).
        """
        diferenca = uniform(-2, 2) + self.criaOutlier()
        somMedida = self.somAtual + diferenca
        timestampSomMedida = datetime.now()
        if not self.outlier(somMedida=somMedida):
            self.somAtual = somMedida
            self.timestampSomAtual = timestampSomMedida
            return {
                'variable': 'som',
                'value': round(self.somAtual, 2),
                'unit': self.escala, 
                'time': self.timestampSomAtual.strftime("%Y-%m-%d, %H:%M:%S")
            }
        else:
            raise Exception("Erro ao medir som!")

    def criaOutlier(self) -> int:
        """
        Gera um outlier com base na chance definida pelo sensor de som.

        Retorna
        -------
            int: Um valor de outlier (80) ou 0, dependendo da chance definida pelo sensor de som.
        """
        chance = randint(0, 80)
        if chance <= self.chanceOutlier:
            return 100
        else:
            return 0

    def outlier(self, somMedida: float) -> bool:
        """
        Verifica se a som medida é um outlier.

        Parâmetros
        ----------
            - somMedida (float): O som medido a ser verificado.

        Retorna
        -------
            bool: True se for um outlier, False caso contrário.
                É considerado outlier quando o som medido é menor que 0 ou maior que 90 decibéis.
        """
        if somMedida < 0 or somMedida > 90:
            self.somAtual = uniform(10, 80)
            self.timestampSomAtual = datetime.now()
            return True
        else:
            return False
