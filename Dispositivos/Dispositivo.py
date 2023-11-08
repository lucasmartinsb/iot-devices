from tagoio_sdk import Device

class Dispositivo():
    def __init__(self, token : str) -> None:
        self.token = token

    def enviaDados(self, dados: dict):
        dadosList = []
        myDevice = Device({ "token": self.token })
        for dado in dados:
            dadosList.append({ "variable" : dado, "value" : dados[dado] })
        result = myDevice.sendData(dadosList)
        return result