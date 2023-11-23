from datetime import datetime
from Dispositivos.Dispositivo import Dispositivo
from random import randint, uniform


class SensorPressao(Dispositivo):
    """
    Simula um sensor de nível de pressao.

    Herda da classe Dispositivo e representa um sensor de pressao que gera
    dados simulados de pressao em uma escala específica.

    Atributos
    ---------
        - chanceOutlier (int): A probabilidade de gerar um outlier.
            Padrão = 5%.
        - pressaoAtual (float): Último pressao medido pelo sensor.
        - timestamppressaoAtual (datetime): O timestamp da última medição de pressao.
    """

    def __init__(self, token: str,  escala: str = "psi",chanceOutlier: int = 5) -> None:
        """
        Inicializador da classe do sensor de pressao.

        Parâmetros
        ----------
            - token (str): Token do dispositivo no TagoIO.
            - chanceOutlier (int): A probabilidade de gerar um outlier.
                Padrão = 5%.
        """
        self.chanceOutlier = chanceOutlier
        self.pressaoAtual = uniform(10, 40)
        self.escala = escala
        self.timestamppressaoAtual = datetime.now()
        super().__init__(token=token)

    def geraDados(self) -> dict:
        """
        Gera dados de pressao simulados.

        Retorna
        -------
            dict: Um dicionário contendo informações sobre o pressao gerado, incluindo
                'variable', 'value' e 'time'.

        Lança
        -----
            Exception: Se ocorrer um erro ao medir o pressao (quando há algum outlier).
        """
        diferenca = uniform(-2, 2) + self.criaOutlier()
        pressaoMedida = self.pressaoAtual + diferenca
        timestampPressaoMedida = datetime.now()
        if not self.outlier(pressaoMedida=pressaoMedida):
            self.pressaoAtual = pressaoMedida
            self.timestampPressaoAtual = timestampPressaoMedida
            return {
                'variable': 'pressao',
                'value': round(self.pressaoAtual, 2),
                'unit': self.escala, 
                'time': self.timestampPressaoAtual.strftime("%Y-%m-%d, %H:%M:%S")
            }
        else:
            raise Exception("Erro ao medir pressao!")

    def criaOutlier(self) -> int:
        """
        Gera um outlier com base na chance definida pelo sensor de pressao.

        Retorna
        -------
            int: Um valor de outlier (40) ou 0, dependendo da chance definida pelo sensor de pressao.
        """
        chance = randint(0, 40)
        if chance <= self.chanceOutlier:
            return 100
        else:
            return 0

    def outlier(self, pressaoMedida: float) -> bool:
        """
        Verifica se a pressao medida é um outlier.

        Parâmetros
        ----------
            - pressaoMedida (float): A pressao medida a ser verificada.

        Retorna
        -------
            bool: True se for um outlier, False caso contrário.
                É considerado outlier quando o pressao medido é menor que 0 ou maior que 50 psi.
        """
        if pressaoMedida < 0 or pressaoMedida > 50:
            self.pressaoAtual = uniform(10, 40)
            self.timestampPressaoAtual = datetime.now()
            return True
        else:
            return False
