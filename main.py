from Dispositivos.SensorPressao import SensorPressao
from Dispositivos.SensorLuminosidade import SensorLuminosidade
from Dispositivos.SensorSom import SensorSom
from Dispositivos.Termometro import Termometro
from Dispositivos.SensorMovimento import SensorMovimento
from Dispositivos.SensorAgua import SensorAgua
from Dispositivos.SensorUmidade import SensorUmidade
from multiprocessing import Process
import datetime
import time

quantidadeExecucoes = 100


def geraDadosTermometro(termometro: Termometro, intervalo: int = 30):
    for _ in range(quantidadeExecucoes):
        time.sleep(intervalo)
        try:
            dados = termometro.geraDados()
            termometro.enviaDados(dados=dados)
            print(f"Termometro - enviado {dados['value']} {dados['unit']}")
        except Exception as e:
            print(e)


def geraDadosSensorAgua(sensorAgua: SensorAgua, intervalo: int = 30):
    for _ in range(quantidadeExecucoes):
        time.sleep(intervalo)
        try:
            dados = sensorAgua.geraDados()
            sensorAgua.enviaDados(dados=dados)
            print(f"SensorAgua - enviado {dados['value']} {dados['unit']}")
        except Exception as e:
            print(e)


def geraDadosSensorUmidade(sensorUmidade: SensorUmidade, intervalo: int = 30):
    for _ in range(quantidadeExecucoes):
        time.sleep(intervalo)
        try:
            dados = sensorUmidade.geraDados()
            sensorUmidade.enviaDados(dados=dados)
            print(f"SensorUmidade - enviado {dados['value']}")
        except Exception as e:
            print(e)


def geraDadosSensorMovimento(sensorMovimento: SensorMovimento, intervalo: int = 15):
    for _ in range(quantidadeExecucoes):
        time.sleep(intervalo)
        try:
            dados = sensorMovimento.geraDados()
            if dados is not None:
                sensorMovimento.enviaDados(dados=dados)
                print(f"SensorMovimento - detectado movimento em intervalo de tempo de alerta")
        except Exception as e:
            print(e)


def geraDadosSensorLuminosidade(sensorLuminosidade: SensorLuminosidade, intervalo: int = 45):
    for _ in range(quantidadeExecucoes):
        time.sleep(intervalo)
        try:
            dados = sensorLuminosidade.geraDados()
            sensorLuminosidade.enviaDados(dados=dados)
            print(f"SensorLuminosidade - enviado {dados['value']}")
        except Exception as e:
            print(e)


def geraDadosSensorSom(sensorSom: SensorSom, intervalo: int = 15):
    for _ in range(quantidadeExecucoes):
        time.sleep(intervalo)
        try:
            dados = sensorSom.geraDados()
            sensorSom.enviaDados(dados=dados)
            print(f"SensorSom - enviado {dados['value']} {dados['unit']}")
        except Exception as e:
            print(e)

def geraDadosSensorPressao(sensorPressao: SensorPressao, intervalo: int = 15):
    for _ in range(quantidadeExecucoes):
        time.sleep(intervalo)
        try:
            dados = sensorPressao.geraDados()
            sensorPressao.enviaDados(dados=dados)
            print(f"SensorPressao - enviado {dados['value']} {dados['unit']}")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    termometro = Termometro(token="e5c937f2-164b-46a1-958c-a2eb2171d75c")
    sensorMovimento = SensorMovimento(token="25f8b7b9-0ef4-453d-bdf0-ace0559b7033",
                                      horarioInicial=datetime.time(16, 00), chanceMovimento=30)
    sensorAgua = SensorAgua(token="719af90e-03ac-4157-9cde-2cd3a05df332")
    sensorUmidade = SensorUmidade(token="0a03cbcc-e913-4482-b996-d129a39844bb")
    sensorLuminosidade = SensorLuminosidade(token="41ac6679-bc76-480f-a8e5-9d1968aa6b1d")
    sensorSom = SensorSom(token="a134722b-1094-4923-9ec0-2d947108af24")
    sensorPressao = SensorPressao(token="2b5251f5-e295-47a8-bf8b-b01ade8721aa")

    processoTermometro = Process(target=geraDadosTermometro, args=(termometro, 10))
    processoSensorMovimento = Process(target=geraDadosSensorMovimento, args=(sensorMovimento, 10))
    processoAgua = Process(target=geraDadosSensorAgua, args=(sensorAgua, 10))
    processoSensorUmidade = Process(target=geraDadosSensorUmidade, args=(sensorUmidade, 10))
    processoLuminosidade = Process(target=geraDadosSensorLuminosidade, args=(sensorLuminosidade, 10))
    processoSom = Process(target=geraDadosSensorSom, args=(sensorSom,10))
    processoPressao = Process(target=geraDadosSensorPressao, args=(sensorPressao, 10))

    processoTermometro.start()
    processoSensorMovimento.start()
    processoAgua.start()
    processoSensorUmidade.start()
    processoLuminosidade.start()
    processoSom.start()
    processoPressao.start()

