from abc import ABC, abstractmethod


class Navegador(ABC):
    @abstractmethod
    def calcular_ruta(self):
        pass

    @abstractmethod
    def mostrar_mapa(self):
        pass


class GPSCarro(Navegador):
    def calcular_ruta(self):
        return "GPS de carro calcula ruta por carreteras."

    def mostrar_mapa(self):
        return "GPS de carro muestra mapa vial."


class GPSAvion(Navegador):
    def calcular_ruta(self):
        return "GPS de avion calcula ruta aerea."

    def mostrar_mapa(self):
        return "GPS de avion muestra mapa aeronautico."


class GPSBarco(Navegador):
    def calcular_ruta(self):
        return "GPS de barco calcula ruta maritima."

    def mostrar_mapa(self):
        return "GPS de barco muestra carta nautica."


def ejecutar_proceso(navegador: Navegador):
    print(navegador.calcular_ruta())
    print(navegador.mostrar_mapa())


if __name__ == "__main__":
    navegadores = [GPSCarro(), GPSAvion(), GPSBarco()]
    for navegador in navegadores:
        ejecutar_proceso(navegador)
        print("-" * 40)
