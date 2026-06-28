from abc import ABC, abstractmethod


class Inversion(ABC):
    @abstractmethod
    def invertir(self):
        pass

    @abstractmethod
    def calcular_ganancia(self):
        pass


class Acciones(Inversion):
    def invertir(self):
        return "Inversion en acciones realizada en mercado bursatil."

    def calcular_ganancia(self):
        return "Ganancia en acciones calculada por variacion de precio."


class Criptomonedas(Inversion):
    def invertir(self):
        return "Inversion en criptomonedas realizada en exchange."

    def calcular_ganancia(self):
        return "Ganancia en criptomonedas calculada por volatilidad."


class Bonos(Inversion):
    def invertir(self):
        return "Inversion en bonos realizada con renta fija."

    def calcular_ganancia(self):
        return "Ganancia en bonos calculada por intereses."


def ejecutar_proceso(inversion: Inversion):
    print(inversion.invertir())
    print(inversion.calcular_ganancia())


if __name__ == "__main__":
    inversiones = [Acciones(), Criptomonedas(), Bonos()]
    for inversion in inversiones:
        ejecutar_proceso(inversion)
        print("-" * 40)
