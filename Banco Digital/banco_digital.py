from abc import ABC, abstractmethod


# POO significa Programacion Orientada a Objetos.
# En POO se crean clases para representar elementos de la vida real.
# En este ejemplo:
# - Cliente representa a una persona del banco.
# - Cuenta representa una cuenta bancaria general.
# - CuentaAhorros y CuentaCorriente son tipos especificos de cuenta.
# - BancoDigital administra clientes y cuentas.
#
# Cada objeto tiene:
# - Atributos: datos del objeto, como nombre, documento y saldo.
# - Metodos: acciones del objeto, como depositar(), retirar() y transferir().


class Cuenta(ABC):
    """Clase abstracta que representa una cuenta bancaria general."""

    # Abstraccion:
    # Cuenta define lo que todas las cuentas deben tener, pero deja algunos
    # detalles para las clases hijas, como el tipo de cuenta.

    def __init__(self, numero: str, titular: "Cliente", saldo: float = 0) -> None:
        # Encapsulamiento:
        # Los datos de la cuenta se guardan dentro del objeto usando self.
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")

        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.movimientos: list[str] = []

    @abstractmethod
    def obtener_tipo(self) -> str:
        """Devuelve el tipo de cuenta."""
        pass

    def depositar(self, monto: float) -> bool:
        """Agrega dinero a la cuenta."""
        if monto <= 0:
            print("El deposito debe ser mayor que cero.")
            return False

        self.saldo += monto
        self.movimientos.append(f"Deposito: +${monto:.2f}")
        print(f"Deposito exitoso. Nuevo saldo: ${self.saldo:.2f}")
        return True

    def retirar(self, monto: float) -> bool:
        """Retira dinero si hay saldo suficiente."""
        if monto <= 0:
            print("El retiro debe ser mayor que cero.")
            return False

        if monto > self.saldo:
            print("Fondos insuficientes.")
            return False

        self.saldo -= monto
        self.movimientos.append(f"Retiro: -${monto:.2f}")
        print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")
        return True

    def transferir(self, cuenta_destino: "Cuenta", monto: float) -> bool:
        """Transfiere dinero desde esta cuenta hacia otra cuenta."""
        if self.retirar(monto):
            cuenta_destino.depositar(monto)
            self.movimientos.append(
                f"Transferencia enviada a {cuenta_destino.numero}: -${monto:.2f}"
            )
            cuenta_destino.movimientos.append(
                f"Transferencia recibida de {self.numero}: +${monto:.2f}"
            )
            print("Transferencia realizada correctamente.")
            return True

        print("No se pudo realizar la transferencia.")
        return False

    def mostrar_info(self) -> None:
        """Muestra informacion general de la cuenta."""
        print(f"\nCuenta: {self.numero}")
        print(f"Tipo: {self.obtener_tipo()}")
        print(f"Titular: {self.titular.nombre}")
        print(f"Saldo: ${self.saldo:.2f}")

    def mostrar_movimientos(self) -> None:
        """Muestra el historial de movimientos."""
        print(f"\nMovimientos de la cuenta {self.numero}:")

        if not self.movimientos:
            print("- No hay movimientos registrados.")
            return

        for movimiento in self.movimientos:
            print(f"- {movimiento}")


class CuentaAhorros(Cuenta):
    """Cuenta bancaria pensada para guardar dinero."""

    # Herencia:
    # CuentaAhorros hereda atributos y metodos de Cuenta.
    # Por eso puede usar depositar(), retirar(), transferir() y mostrar_info().

    def obtener_tipo(self) -> str:
        # Polimorfismo:
        # Todas las cuentas tienen obtener_tipo(), pero cada clase hija
        # devuelve un resultado diferente.
        return "Cuenta de ahorros"

    def aplicar_interes(self, porcentaje: float) -> bool:
        """Aplica un interes positivo al saldo de la cuenta."""
        if porcentaje <= 0:
            print("El porcentaje de interes debe ser mayor que cero.")
            return False

        interes = self.saldo * porcentaje / 100
        self.saldo += interes
        self.movimientos.append(f"Interes aplicado: +${interes:.2f}")
        print(f"Interes aplicado. Nuevo saldo: ${self.saldo:.2f}")
        return True


class CuentaCorriente(Cuenta):
    """Cuenta bancaria para movimientos frecuentes."""

    def obtener_tipo(self) -> str:
        return "Cuenta corriente"


class Cliente:
    """Representa a un cliente del banco."""

    def __init__(self, nombre: str, documento: str) -> None:
        self.nombre = nombre
        self.documento = documento
        # Composicion:
        # Un cliente contiene o administra una lista de cuentas.
        self.cuentas: list[Cuenta] = []

    def agregar_cuenta(self, cuenta: Cuenta) -> None:
        """Asocia una cuenta al cliente."""
        self.cuentas.append(cuenta)

    def mostrar_cuentas(self) -> None:
        """Muestra las cuentas del cliente."""
        print(f"\nCuentas de {self.nombre}:")

        if not self.cuentas:
            print("- No tiene cuentas registradas.")
            return

        for cuenta in self.cuentas:
            print(f"- {cuenta.numero} ({cuenta.obtener_tipo()}) - ${cuenta.saldo:.2f}")

    def __str__(self) -> str:
        return f"{self.nombre} - Documento {self.documento}"


class BancoDigital:
    """Administra clientes y cuentas de un banco digital."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.clientes: list[Cliente] = []
        self.cuentas: list[Cuenta] = []

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un cliente en el banco."""
        self.clientes.append(cliente)

    def abrir_cuenta(self, cliente: Cliente, cuenta: Cuenta) -> None:
        """Registra una cuenta en el banco y la asocia a un cliente."""
        self.cuentas.append(cuenta)
        cliente.agregar_cuenta(cuenta)

    def buscar_cuenta(self, numero: str) -> Cuenta | None:
        """Busca una cuenta por numero."""
        for cuenta in self.cuentas:
            if cuenta.numero == numero:
                return cuenta
        return None

    def mostrar_resumen(self) -> None:
        """Muestra clientes y cuentas registrados."""
        print(f"\n=== {self.nombre} ===")

        print("\nClientes registrados:")
        if not self.clientes:
            print("- No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(f"- {cliente}")

        print("\nCuentas registradas:")
        if not self.cuentas:
            print("- No hay cuentas registradas.")
        else:
            for cuenta in self.cuentas:
                print(
                    f"- {cuenta.numero} | {cuenta.obtener_tipo()} | "
                    f"{cuenta.titular.nombre} | ${cuenta.saldo:.2f}"
                )


def main() -> None:
    """Punto de entrada del programa."""
    banco = BancoDigital("Banco Digital SENA")

    cliente_1 = Cliente("Laura Gomez", "1001234567")
    cliente_2 = Cliente("Carlos Ruiz", "1007654321")

    banco.registrar_cliente(cliente_1)
    banco.registrar_cliente(cliente_2)

    cuenta_ahorros = CuentaAhorros("AH-001", cliente_1, 500000)
    cuenta_corriente = CuentaCorriente("CC-001", cliente_2, 300000)

    banco.abrir_cuenta(cliente_1, cuenta_ahorros)
    banco.abrir_cuenta(cliente_2, cuenta_corriente)

    cuenta_ahorros.depositar(150000)
    cuenta_corriente.retirar(50000)
    cuenta_ahorros.transferir(cuenta_corriente, 100000)
    cuenta_ahorros.aplicar_interes(2)

    banco.mostrar_resumen()
    cliente_1.mostrar_cuentas()
    cliente_2.mostrar_cuentas()
    cuenta_ahorros.mostrar_movimientos()
    cuenta_corriente.mostrar_movimientos()


# Esta condicion permite importar las clases desde otro archivo sin ejecutar
# automaticamente el programa principal.
if __name__ == "__main__":
    main()
