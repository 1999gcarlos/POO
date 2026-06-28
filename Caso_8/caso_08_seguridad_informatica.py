from abc import ABC, abstractmethod


class SistemaSeguridad(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def escanear(self):
        pass

    @abstractmethod
    def bloquear_amenaza(self):
        pass


class Antivirus(SistemaSeguridad):
    def escanear(self):
        return "Antivirus escaneando archivos."

    def bloquear_amenaza(self):
        return "Virus bloqueado."


class Firewall(SistemaSeguridad):
    def escanear(self):
        return "Firewall revisando trafico."

    def bloquear_amenaza(self):
        return "Conexion sospechosa bloqueada."


class IDS(SistemaSeguridad):
    def escanear(self):
        return "IDS detectando intrusiones."

    def bloquear_amenaza(self):
        return "Intrusion reportada y bloqueada."


def main():
    sistemas = []

    while True:
        print("\n--- Seguridad informatica ---")
        print("1. Registrar antivirus")
        print("2. Registrar firewall")
        print("3. Registrar IDS")
        print("4. Escanear y bloquear")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            nombre = input("Nombre del sistema: ")
            if opcion == "1":
                sistema = Antivirus(nombre)
            elif opcion == "2":
                sistema = Firewall(nombre)
            else:
                sistema = IDS(nombre)
            sistemas.append(sistema)
            print("Sistema registrado.")

        elif opcion == "4":
            if not sistemas:
                print("No hay sistemas registrados.")
            for sistema in sistemas:
                print(sistema.escanear())
                print(sistema.bloquear_amenaza())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
