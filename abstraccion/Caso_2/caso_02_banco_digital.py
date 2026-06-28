from abc import ABC, abstractmethod


class CuentaBancaria(ABC):
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def retirar(self, monto):
        if monto <= 0:
            return "El monto debe ser positivo."
        if monto > self.saldo:
            return "Fondos insuficientes."
        self.saldo -= monto
        return f"Retiro exitoso. Saldo: {self.saldo}"

    def depositar(self, monto):
        if monto <= 0:
            return "El monto debe ser positivo."
        self.saldo += monto
        return f"Deposito exitoso. Saldo: {self.saldo}"

    @abstractmethod
    def calcular_interes(self):
        pass


class CuentaAhorros(CuentaBancaria):
    def calcular_interes(self):
        return self.saldo * 0.03


class CuentaCorriente(CuentaBancaria):
    def calcular_interes(self):
        return self.saldo * 0.01


class CuentaEmpresarial(CuentaBancaria):
    def calcular_interes(self):
        return self.saldo * 0.05


def main():
    cuentas = []

    while True:
        print("\n--- Banco digital ---")
        print("1. Crear cuenta de ahorros")
        print("2. Crear cuenta corriente")
        print("3. Crear cuenta empresarial")
        print("4. Depositar")
        print("5. Retirar")
        print("6. Ver cuentas")
        print("7. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            numero = input("Numero de cuenta: ")
            titular = input("Titular: ")
            saldo = float(input("Saldo inicial: "))

            if opcion == "1":
                cuenta = CuentaAhorros(numero, titular, saldo)
            elif opcion == "2":
                cuenta = CuentaCorriente(numero, titular, saldo)
            else:
                cuenta = CuentaEmpresarial(numero, titular, saldo)

            cuentas.append(cuenta)
            print("Cuenta creada.")

        elif opcion in ["4", "5"]:
            numero = input("Numero de cuenta: ")
            cuenta = next((c for c in cuentas if c.numero == numero), None)
            if cuenta is None:
                print("Cuenta no encontrada.")
                continue
            monto = float(input("Monto: "))
            print(cuenta.depositar(monto) if opcion == "4" else cuenta.retirar(monto))

        elif opcion == "6":
            if not cuentas:
                print("No hay cuentas registradas.")
            for cuenta in cuentas:
                print(f"{cuenta.numero} | {cuenta.titular} | Saldo: {cuenta.saldo} | Interes: {cuenta.calcular_interes()}")

        elif opcion == "7":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
