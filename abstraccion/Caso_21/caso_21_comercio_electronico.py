from abc import ABC, abstractmethod


class PedidoOnline(ABC):
    def __init__(self, cliente, subtotal):
        self.cliente = cliente
        self.subtotal = subtotal

    @abstractmethod
    def calcular_envio(self):
        pass

    @abstractmethod
    def confirmar_pago(self):
        pass


class PedidoNacional(PedidoOnline):
    def calcular_envio(self):
        return 8

    def confirmar_pago(self):
        return f"Pago nacional confirmado para {self.cliente}."


class PedidoInternacional(PedidoOnline):
    def calcular_envio(self):
        return 25

    def confirmar_pago(self):
        return f"Pago internacional confirmado para {self.cliente}."


def main():
    pedidos = []

    while True:
        print("\n--- Comercio electronico ---")
        print("1. Registrar pedido nacional")
        print("2. Registrar pedido internacional")
        print("3. Confirmar pedidos")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2"]:
            cliente = input("Cliente: ")
            subtotal = float(input("Subtotal: "))
            if opcion == "1":
                pedido = PedidoNacional(cliente, subtotal)
            else:
                pedido = PedidoInternacional(cliente, subtotal)
            pedidos.append(pedido)
            print("Pedido registrado.")

        elif opcion == "3":
            if not pedidos:
                print("No hay pedidos registrados.")
            for pedido in pedidos:
                total = pedido.subtotal + pedido.calcular_envio()
                print(pedido.confirmar_pago())
                print(f"Total con envio: {total}")

        elif opcion == "4":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
