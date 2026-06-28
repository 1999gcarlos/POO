from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, placa, kilometros):
        self.placa = placa
        self.kilometros = kilometros

    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def detener(self):
        pass

    @abstractmethod
    def calcular_combustible(self):
        pass


class Bus(Vehiculo):
    def arrancar(self):
        return f"Bus {self.placa} arrancando."

    def detener(self):
        return f"Bus {self.placa} detenido."

    def calcular_combustible(self):
        return self.kilometros / 8


class Taxi(Vehiculo):
    def arrancar(self):
        return f"Taxi {self.placa} arrancando."

    def detener(self):
        return f"Taxi {self.placa} detenido."

    def calcular_combustible(self):
        return self.kilometros / 14


class Camion(Vehiculo):
    def arrancar(self):
        return f"Camion {self.placa} arrancando."

    def detener(self):
        return f"Camion {self.placa} detenido."

    def calcular_combustible(self):
        return self.kilometros / 6


def main():
    vehiculos = []

    while True:
        print("\n--- Empresa de transporte ---")
        print("1. Registrar bus")
        print("2. Registrar taxi")
        print("3. Registrar camion")
        print("4. Operar vehiculos")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            placa = input("Placa: ")
            kilometros = float(input("Kilometros a recorrer: "))
            if opcion == "1":
                vehiculo = Bus(placa, kilometros)
            elif opcion == "2":
                vehiculo = Taxi(placa, kilometros)
            else:
                vehiculo = Camion(placa, kilometros)
            vehiculos.append(vehiculo)
            print("Vehiculo registrado.")

        elif opcion == "4":
            if not vehiculos:
                print("No hay vehiculos registrados.")
            for vehiculo in vehiculos:
                print(vehiculo.arrancar())
                print(f"Combustible: {vehiculo.calcular_combustible():.2f} galones")
                print(vehiculo.detener())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
