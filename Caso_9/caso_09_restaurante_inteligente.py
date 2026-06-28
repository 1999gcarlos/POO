from abc import ABC, abstractmethod


class Pedido(ABC):
    def __init__(self, cliente, subtotal):
        self.cliente = cliente
        self.subtotal = subtotal

    @abstractmethod
    def calcular_total(self):
        pass

    @abstractmethod
    def generar_factura(self):
        pass


class PedidoMesa(Pedido):
    def calcular_total(self):
        return self.subtotal

    def generar_factura(self):
        return f"Factura mesa para {self.cliente}: {self.calcular_total()}"


class PedidoDomicilio(Pedido):
    def calcular_total(self):
        return self.subtotal + 5

    def generar_factura(self):
        return f"Factura domicilio para {self.cliente}: {self.calcular_total()}"


class PedidoExpress(Pedido):
    def calcular_total(self):
        return self.subtotal + 10

    def generar_factura(self):
        return f"Factura express para {self.cliente}: {self.calcular_total()}"


def main():
    pedidos = []

    while True:
        print("\n--- Restaurante inteligente ---")
        print("1. Registrar pedido de mesa")
        print("2. Registrar pedido a domicilio")
        print("3. Registrar pedido express")
        print("4. Generar facturas")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            cliente = input("Cliente: ")
            subtotal = float(input("Subtotal: "))
            if opcion == "1":
                pedido = PedidoMesa(cliente, subtotal)
            elif opcion == "2":
                pedido = PedidoDomicilio(cliente, subtotal)
            else:
                pedido = PedidoExpress(cliente, subtotal)
            pedidos.append(pedido)
            print("Pedido registrado.")

        elif opcion == "4":
            if not pedidos:
                print("No hay pedidos registrados.")
            for pedido in pedidos:
                print(pedido.generar_factura())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
