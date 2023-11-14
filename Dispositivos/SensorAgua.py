from datetime import datetime
from Dispositivos.Dispositivo import Dispositivo
from random import randint

class SensorAgua(Dispositivo):
    """
    Simula um sensor de nível de água.

    Herda da classe Dispositivo e representa um sensor de nível de água que gera
    dados simulados de nível em uma escala específica.

    Atributos
    ---------
        - escala (str): A escala de nível de água utilizada.
            Padrão = Litros ("L").
        - chanceOutlier (int): A probabilidade de gerar um outlier.
            Padrão = 5%.
        - nivelMaximo (int): O nível máximo de água que o sensor pode medir.
            Padrão = 100.
        - nivelAtual (int): Último nível de água medido pelo sensor.
        - timestampNivelAtual (datetime): O timestamp da última medição de nível de água.
    """

    def __init__(self, token: str, escala: str = "L", chanceOutlier: int = 5, nivelMaximo: int = 100) -> None:
        """
        Inicializador da classe do sensor de água.

        Parâmetros
        ----------
            - token (str): Token do dispositivo no TagoIO.
            - escala (str): A escala de nível de água utilizada.
                Padrão = Litros ("L").
            - chanceOutlier (int): A probabilidade de gerar um outlier.
                Padrão = 5%.
            - nivelMaximo (int): O nível máximo de água que o sensor pode medir.
                Padrão = 100.
        """
        self.nivelMaximo = nivelMaximo
        self.chanceOutlier = chanceOutlier
        self.escala = escala
        self.nivelAtual = randint(0, nivelMaximo)
        self.timestampNivelAtual = datetime.now()
        super().__init__(token=token)
    
    def geraDados(self) -> dict:
        """
        Gera dados de nível de água simulados.

        Retorna
        -------
            dict: Um dicionário contendo informações sobre o nível de água gerado, incluindo
                'variable', 'value', 'unit' e 'time'.
        
        Lança
        -----
            Exception: Se ocorrer um erro ao medir o nível de água (quando há algum outlier).
        """
        diferenca = randint(-5, 5) + self.criaOutlier()
        nivelMedido = self.nivelAtual + diferenca
        timestampNivelMedido = datetime.now()
        if not self.outlier(nivelMedido=nivelMedido):
            self.nivelAtual = nivelMedido
            self.timestampNivelAtual = timestampNivelMedido
            return {
                'variable': 'NivelAgua',
                'value': self.nivelAtual, 
                'unit': self.escala, 
                'time': self.timestampNivelAtual.strftime("%Y-%m-%d, %H:%M:%S")
            }
        else:
            raise Exception("Erro ao medir nível!")
    
    def criaOutlier(self) -> int:
        """
        Gera um outlier com base na chance definida pelo sensor de água.

        Retorna
        -------
            int: Um valor de outlier (maior que o nível máximo) ou 0, dependendo da chance definida pelo sensor de água.
        """
        chance = randint(0, 100)
        if chance <= self.chanceOutlier:
            return self.nivelMaximo + 1
        else:
            return 0
        
    def outlier(self, nivelMedido: int) -> bool:
        """
        Verifica se o nível de água medido é um outlier. 

        Parâmetros
        ----------
            - nivelMedido (int): O nível de água medido a ser verificado.

        Retorna
        -------
            bool: True se for um outlier, False caso contrário.
                É considerado outlier quando a diferença entre o nível medido com o atual é maior que o nível máximo ou o valor medido é menor que 0.
        """
        if nivelMedido - self.nivelAtual > self.nivelMaximo:
            return True
        if nivelMedido < 0:
            self.nivelAtual = 50
            return True
        if nivelMedido > self.nivelMaximo:
            self.nivelAtual = 0
            return True
        else:
            return False
