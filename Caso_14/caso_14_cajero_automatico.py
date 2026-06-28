from abc import ABC, abstractmethod


class Transaccion(ABC):
    def __init__(self, cuenta, monto):
        self.cuenta = cuenta
        self.monto = monto

    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def generar_comprobante(self):
        pass


class Retiro(Transaccion):
    def ejecutar(self):
        return f"Retiro de {self.monto} en cuenta {self.cuenta}."

    def generar_comprobante(self):
        return "Comprobante de retiro generado."


class Deposito(Transaccion):
    def ejecutar(self):
        return f"Deposito de {self.monto} en cuenta {self.cuenta}."

    def generar_comprobante(self):
        return "Comprobante de deposito generado."


class Transferencia(Transaccion):
    def ejecutar(self):
        return f"Transferencia de {self.monto} desde cuenta {self.cuenta}."

    def generar_comprobante(self):
        return "Comprobante de transferencia generado."


def main():
    transacciones = []

    while True:
        print("\n--- Cajero automatico ---")
        print("1. Registrar retiro")
        print("2. Registrar deposito")
        print("3. Registrar transferencia")
        print("4. Ejecutar transacciones")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            cuenta = input("Cuenta: ")
            monto = float(input("Monto: "))
            if opcion == "1":
                transaccion = Retiro(cuenta, monto)
            elif opcion == "2":
                transaccion = Deposito(cuenta, monto)
            else:
                transaccion = Transferencia(cuenta, monto)
            transacciones.append(transaccion)
            print("Transaccion registrada.")

        elif opcion == "4":
            if not transacciones:
                print("No hay transacciones registradas.")
            for transaccion in transacciones:
                print(transaccion.ejecutar())
                print(transaccion.generar_comprobante())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
