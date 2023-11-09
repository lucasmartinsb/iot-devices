from Dispositivos.Termometro import Termometro
import time

if __name__ == '__main__':
    termometro = Termometro(token="e5c937f2-164b-46a1-958c-a2eb2171d75c")
    for _ in range(5):
        time.sleep(5)
        try:
            print(termometro.enviaDados(dados=termometro.geraDados()))
        except Exception as e:
            print(e)