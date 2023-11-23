from datetime import datetime
from Dispositivos.Dispositivo import Dispositivo
from random import randint, uniform


class SensorLuminosidade(Dispositivo):
    """
    Simula um sensor de luminosidade.

    Herda da classe Dispositivo e representa um sensor de luminosidade que gera
    dados simulados de luminosidade em uma escala específica.

    Atributos
    ---------
        - chanceOutlier (int): A probabilidade de gerar um outlier.
            Padrão = 5%.
        - luminosidadeAtual (float): Última luminosidade medida pelo sensor.
        - timestampluminosidadeAtual (datetime): O timestamp da última medição de luminosidade.
    """

    def __init__(self, token: str, chanceOutlier: int = 5) -> None:
        """
        Inicializador da classe do sensor de luminosidade.

        Parâmetros
        ----------
            - token (str): Token do dispositivo no TagoIO.
            - chanceOutlier (int): A probabilidade de gerar um outlier.
                Padrão = 5%.
        """
        self.chanceOutlier = chanceOutlier
        self.luminosidadeAtual = uniform(10, 90)
        self.timestampluminosidadeAtual = datetime.now()
        super().__init__(token=token)

    def geraDados(self) -> dict:
        """
        Gera dados de luminosidade simulados.

        Retorna
        -------
            dict: Um dicionário contendo informações sobre a luminosidade gerada, incluindo
                'variable', 'value' e 'time'.

        Lança
        -----
            Exception: Se ocorrer um erro ao medir a luminosidade (quando há algum outlier).
        """
        diferenca = uniform(-2, 2) + self.criaOutlier()
        luminosidadeMedida = self.luminosidadeAtual + diferenca
        timestampLuminosidadeMedida = datetime.now()
        if not self.outlier(luminosidadeMedida=luminosidadeMedida):
            self.luminosidadeAtual = luminosidadeMedida
            self.timestampLuminosidadeAtual = timestampLuminosidadeMedida
            return {
                'variable': 'luminosidade',
                'value': round(self.luminosidadeAtual, 2),
                'time': self.timestampLuminosidadeAtual.strftime("%Y-%m-%d, %H:%M:%S")
            }
        else:
            raise Exception("Erro ao medir luminosidade!")

    def criaOutlier(self) -> int:
        """
        Gera um outlier com base na chance definida pelo sensor de luminosidade.

        Retorna
        -------
            int: Um valor de outlier (100000) ou 0, dependendo da chance definida pelo sensor de luminosidade.
        """
        chance = randint(0, 100000)
        if chance <= self.chanceOutlier:
            return 100
        else:
            return 0

    def outlier(self, luminosidadeMedida: float) -> bool:
        """
        Verifica se a luminosidade medida é um outlier.

        Parâmetros
        ----------
            - luminosidadeMedida (float): A luminosidade medida a ser verificada.

        Retorna
        -------
            bool: True se for um outlier, False caso contrário.
                É considerado outlier quando a luminosidade medida é menor que 0 ou maior que 100000.
        """
        if luminosidadeMedida < 0 or luminosidadeMedida > 100000:
            self.luminosidadeAtual = uniform(10, 99990)
            self.timestampLuminosidadeAtual = datetime.now()
            return True
        else:
            return False
