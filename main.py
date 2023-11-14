from Dispositivos.Termometro import Termometro
from Dispositivos.SensorMovimento import SensorMovimento
from Dispositivos.SensorAgua import SensorAgua
from multiprocessing import Process
import datetime
import time

def geraDadosTermometro(termometro : Termometro, intervalo : int = 30):
    for _ in range(10):
        time.sleep(intervalo)
        try:
            dados = termometro.geraDados()
            termometro.enviaDados(dados=dados)
            print(f"Termometro - enviado {dados['value']} {dados['unit']}")
        except Exception as e:
            print(e)
            
def geraDadosSensorAgua(sensorAgua : SensorAgua, intervalo : int = 30):
    for _ in range(10):
        time.sleep(intervalo)
        try:
            dados = sensorAgua.geraDados()
            sensorAgua.enviaDados(dados=dados)
            print(f"SensorAgua - enviado {dados['value']} {dados['unit']}")
        except Exception as e:
            print(e)

def geraDadosSensorMovimento(sensorMovimento : SensorMovimento, intervalo : int = 15):
    for _ in range(10):
        time.sleep(intervalo)
        try:
            dados = sensorMovimento.geraDados()
            if dados != None:
                sensorMovimento.enviaDados(dados=dados)
                print(f"SensorMovimento - detectado movimento em intervalo de tempo de alerta")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    termometro = Termometro(token="e5c937f2-164b-46a1-958c-a2eb2171d75c")
    sensorMovimento = SensorMovimento(token="25f8b7b9-0ef4-453d-bdf0-ace0559b7033", horarioInicial=datetime.time(16,00),chanceMovimento=50)
    sensorAgua = SensorAgua(token="719af90e-03ac-4157-9cde-2cd3a05df332")
    
    processoTermometro = Process(target=geraDadosTermometro, args=(termometro, 10))
    processoSensorMovimento = Process(target=geraDadosSensorMovimento, args=(sensorMovimento, 10))
    processoAgua = Process(target=geraDadosSensorAgua, args=(sensorAgua, 10))

    processoTermometro.start()
    processoSensorMovimento.start()
    processoAgua.start()