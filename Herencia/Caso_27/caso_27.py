from abc import ABC, abstractmethod


class MisionEspacial(ABC):
    @abstractmethod
    def despegar(self):
        pass

    @abstractmethod
    def aterrizar(self):
        pass


class MisionLunar(MisionEspacial):
    def despegar(self):
        return "Mision lunar despega hacia la orbita de la Luna."

    def aterrizar(self):
        return "Mision lunar aterriza sobre superficie lunar."


class MisionMarte(MisionEspacial):
    def despegar(self):
        return "Mision a Marte despega con trayectoria interplanetaria."

    def aterrizar(self):
        return "Mision a Marte aterriza con modulo especializado."


class MisionSatelital(MisionEspacial):
    def despegar(self):
        return "Mision satelital despega para poner satelite en orbita."

    def aterrizar(self):
        return "Mision satelital completa retorno o cierre orbital."


def ejecutar_proceso(mision: MisionEspacial):
    print(mision.despegar())
    print(mision.aterrizar())


if __name__ == "__main__":
    misiones = [MisionLunar(), MisionMarte(), MisionSatelital()]
    for mision in misiones:
        ejecutar_proceso(mision)
        print("-" * 40)
