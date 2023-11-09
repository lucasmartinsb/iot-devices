from tagoio_sdk import Device

class Dispositivo():
    """
    Classe que representa um dispositivo para envio de dados usando a biblioteca tagoio_sdk.

    Atributos
    ---------
        - token (str): O token de autenticação do dispositivo.
        - fila (list): Uma lista para armazenar os dados a serem enviados.
    """

    def __init__(self, token: str) -> None:
        """
        Inicializa uma instância da classe Dispositivo.

        Parâmetros
        ----------
            - token (str): O token de autenticação do dispositivo.
        """
        self.token = token
        self.fila = []

    def enviaDados(self, dados: dict):
        """
        Adiciona dados à fila e os envia para o token TagoIO definido.

        Parâmetros
        ----------
            - dados (dict): Um dicionário contendo os dados a serem enviados.

        Retorna
        -------
            dict: O resultado do envio dos dados.
            str: Um texto do erro gerado pelo envio 
                (os dados continuam armazenados na fila)

        Lança:
            Exception: Se ocorrer um erro durante o envio dos dados.
        """
        dispositivo = Device({"token": self.token})
        self.fila.append(dados)
        try:
            resultado = dispositivo.sendData(self.fila)
            self.fila = []
            return resultado
        except Exception as e:
            return e