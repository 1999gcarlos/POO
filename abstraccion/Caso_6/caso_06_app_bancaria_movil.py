from abc import ABC, abstractmethod


class MetodoPago(ABC):
    def __init__(self, usuario, monto):
        self.usuario = usuario
        self.monto = monto

    @abstractmethod
    def pagar(self):
        pass

    @abstractmethod
    def validar_pago(self):
        pass


class Nequi(MetodoPago):
    def validar_pago(self):
        return self.monto > 0

    def pagar(self):
        return f"Pago por Nequi realizado por {self.usuario}."


class Paypal(MetodoPago):
    def validar_pago(self):
        return self.monto > 0

    def pagar(self):
        return f"Pago por Paypal realizado por {self.usuario}."


class TarjetaCredito(MetodoPago):
    def validar_pago(self):
        return self.monto > 0

    def pagar(self):
        return f"Pago con tarjeta realizado por {self.usuario}."


def main():
    pagos = []

    while True:
        print("\n--- Aplicacion bancaria movil ---")
        print("1. Pagar con Nequi")
        print("2. Pagar con Paypal")
        print("3. Pagar con tarjeta de credito")
        print("4. Ver pagos")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            usuario = input("Usuario: ")
            monto = float(input("Monto: "))
            if opcion == "1":
                pago = Nequi(usuario, monto)
            elif opcion == "2":
                pago = Paypal(usuario, monto)
            else:
                pago = TarjetaCredito(usuario, monto)
            pagos.append(pago)
            print(pago.pagar() if pago.validar_pago() else "Pago invalido.")

        elif opcion == "4":
            if not pagos:
                print("No hay pagos registrados.")
            for pago in pagos:
                print(f"{pago.__class__.__name__} | {pago.usuario} | {pago.monto}")

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
