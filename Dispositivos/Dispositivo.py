from tagoio_sdk import Device

class Dispositivo():
    def __init__(self, token : str) -> None:
        self.token = token

    def enviaDados(self, dados: dict):
        myDevice = Device({ "token": self.token })
        result = myDevice.sendData(dados)
        return result