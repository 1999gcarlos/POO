from abc import ABC, abstractmethod


class Restaurante(ABC):
    @abstractmethod
    def abrir_restaurante(self):
        pass

    @abstractmethod
    def recibir_pedido(self):
        pass


class RestauranteRapido(Restaurante):
    def abrir_restaurante(self):
        return "Restaurante rapido abre con menu de atencion inmediata."

    def recibir_pedido(self):
        return "Restaurante rapido recibe un pedido para entrega express."


class RestauranteGourmet(Restaurante):
    def abrir_restaurante(self):
        return "Restaurante gourmet abre con servicio especializado."

    def recibir_pedido(self):
        return "Restaurante gourmet recibe un pedido personalizado."


class RestauranteVegetariano(Restaurante):
    def abrir_restaurante(self):
        return "Restaurante vegetariano abre con opciones saludables."

    def recibir_pedido(self):
        return "Restaurante vegetariano recibe un pedido sin carne."


def ejecutar_proceso(restaurante: Restaurante):
    print(restaurante.abrir_restaurante())
    print(restaurante.recibir_pedido())


if __name__ == "__main__":
    restaurantes = [RestauranteRapido(), RestauranteGourmet(), RestauranteVegetariano()]
    for restaurante in restaurantes:
        ejecutar_proceso(restaurante)
        print("-" * 40)
