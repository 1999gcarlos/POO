from abc import ABC, abstractmethod


class Producto(ABC):
    @abstractmethod
    def calcular_precio(self):
        pass

    @abstractmethod
    def verificar_stock(self):
        pass


class Lacteo(Producto):
    def calcular_precio(self):
        return "Precio del lacteo calculado con control de vencimiento."

    def verificar_stock(self):
        return "Stock de lacteos verificado en refrigeracion."


class Bebida(Producto):
    def calcular_precio(self):
        return "Precio de la bebida calculado segun presentacion."

    def verificar_stock(self):
        return "Stock de bebidas verificado en bodega."


class Enlatado(Producto):
    def calcular_precio(self):
        return "Precio del enlatado calculado por unidad."

    def verificar_stock(self):
        return "Stock de enlatados verificado en estanteria."


def ejecutar_proceso(producto: Producto):
    print(producto.calcular_precio())
    print(producto.verificar_stock())


if __name__ == "__main__":
    productos = [Lacteo(), Bebida(), Enlatado()]
    for producto in productos:
        ejecutar_proceso(producto)
        print("-" * 40)
