from abc import ABC, abstractmethod


class Bodega(ABC):
    @abstractmethod
    def almacenar(self):
        pass

    @abstractmethod
    def despachar(self):
        pass


class BodegaFria(Bodega):
    def almacenar(self):
        return "Bodega fria almacena productos con temperatura controlada."

    def despachar(self):
        return "Bodega fria despacha conservando cadena de frio."


class BodegaSeca(Bodega):
    def almacenar(self):
        return "Bodega seca almacena productos no perecederos."

    def despachar(self):
        return "Bodega seca despacha mercancia general."


class BodegaAutomatizada(Bodega):
    def almacenar(self):
        return "Bodega automatizada almacena usando sistemas roboticos."

    def despachar(self):
        return "Bodega automatizada despacha con seleccion automatica."


def ejecutar_proceso(bodega: Bodega):
    print(bodega.almacenar())
    print(bodega.despachar())


if __name__ == "__main__":
    bodegas = [BodegaFria(), BodegaSeca(), BodegaAutomatizada()]
    for bodega in bodegas:
        ejecutar_proceso(bodega)
        print("-" * 40)
