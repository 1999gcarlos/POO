from abc import ABC, abstractmethod


class Impresora(ABC):
    @abstractmethod
    def imprimir(self):
        pass

    @abstractmethod
    def cancelar_impresion(self):
        pass


class ImpresoraLaser(Impresora):
    def imprimir(self):
        return "Impresora laser imprime documentos de alta velocidad."

    def cancelar_impresion(self):
        return "Impresion laser cancelada en la cola de trabajos."


class Impresora3D(Impresora):
    def imprimir(self):
        return "Impresora 3D fabrica una pieza por capas."

    def cancelar_impresion(self):
        return "Impresion 3D cancelada y material detenido."


class ImpresoraTinta(Impresora):
    def imprimir(self):
        return "Impresora de tinta imprime imagenes a color."

    def cancelar_impresion(self):
        return "Impresion de tinta cancelada correctamente."


def ejecutar_proceso(impresora: Impresora):
    print(impresora.imprimir())
    print(impresora.cancelar_impresion())


if __name__ == "__main__":
    impresoras = [ImpresoraLaser(), Impresora3D(), ImpresoraTinta()]
    for impresora in impresoras:
        ejecutar_proceso(impresora)
        print("-" * 40)
