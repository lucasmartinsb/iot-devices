from Dispositivos.Termometro import Termometro
import time

if __name__ == '__main__':
    termometro = Termometro(escala="c")
    for _ in range(5):
        time.sleep(60)
        try:
            print(termometro.enviaDados(dados=termometro.geraDados()))
        except Exception as e:
            print(e)