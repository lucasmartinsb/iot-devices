from tagoio_sdk import Device

class Dispositivo():
    def __init__(self, token : str) -> None:
        self.token = token
        self.fila = []

    def enviaDados(self, dados: dict):
        dispositivo = Device({ "token" : self.token })
        self.fila.append(dados)
        try:
            resultado = dispositivo.sendData(self.fila)
            self.fila = []
            return resultado
        except Exception as e:
            return e