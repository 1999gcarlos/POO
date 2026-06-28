from abc import ABC, abstractmethod


class Funcion(ABC):
    @abstractmethod
    def iniciar_funcion(self):
        pass

    @abstractmethod
    def vender_boletos(self):
        pass


class Funcion2D(Funcion):
    def iniciar_funcion(self):
        return "Funcion 2D iniciada en sala tradicional."

    def vender_boletos(self):
        return "Boletos para funcion 2D vendidos a tarifa normal."


class Funcion3D(Funcion):
    def iniciar_funcion(self):
        return "Funcion 3D iniciada con gafas especiales."

    def vender_boletos(self):
        return "Boletos para funcion 3D vendidos con recargo."


class FuncionVIP(Funcion):
    def iniciar_funcion(self):
        return "Funcion VIP iniciada con servicio preferencial."

    def vender_boletos(self):
        return "Boletos VIP vendidos con asiento premium."


def ejecutar_proceso(funcion: Funcion):
    print(funcion.iniciar_funcion())
    print(funcion.vender_boletos())


if __name__ == "__main__":
    funciones = [Funcion2D(), Funcion3D(), FuncionVIP()]
    for funcion in funciones:
        ejecutar_proceso(funcion)
        print("-" * 40)
