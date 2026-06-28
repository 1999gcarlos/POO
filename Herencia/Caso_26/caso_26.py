from abc import ABC, abstractmethod


class Residuo(ABC):
    @abstractmethod
    def clasificar(self):
        pass

    @abstractmethod
    def reciclar(self):
        pass


class Plastico(Residuo):
    def clasificar(self):
        return "Residuo plastico clasificado por tipo de polimero."

    def reciclar(self):
        return "Residuo plastico reciclado mediante trituracion."


class Vidrio(Residuo):
    def clasificar(self):
        return "Residuo de vidrio clasificado por color."

    def reciclar(self):
        return "Residuo de vidrio reciclado por fundicion."


class Papel(Residuo):
    def clasificar(self):
        return "Residuo de papel clasificado por calidad."

    def reciclar(self):
        return "Residuo de papel reciclado para nueva pulpa."


def ejecutar_proceso(residuo: Residuo):
    print(residuo.clasificar())
    print(residuo.reciclar())


if __name__ == "__main__":
    residuos = [Plastico(), Vidrio(), Papel()]
    for residuo in residuos:
        ejecutar_proceso(residuo)
        print("-" * 40)
