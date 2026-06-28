from abc import ABC, abstractmethod


class Entrega(ABC):
    def __init__(self, destino, distancia):
        self.destino = destino
        self.distancia = distancia

    @abstractmethod
    def calcular_tiempo(self):
        pass

    @abstractmethod
    def asignar_repartidor(self):
        pass


class EntregaMoto(Entrega):
    def calcular_tiempo(self):
        return round(self.distancia / 40 * 60)

    def asignar_repartidor(self):
        return "Repartidor en moto"


class EntregaBicicleta(Entrega):
    def calcular_tiempo(self):
        return round(self.distancia / 15 * 60)

    def asignar_repartidor(self):
        return "Repartidor en bicicleta"


class EntregaCarro(Entrega):
    def calcular_tiempo(self):
        return round(self.distancia / 30 * 60)

    def asignar_repartidor(self):
        return "Repartidor en carro"


def main():
    entregas = []

    while True:
        print("\n--- Plataforma de domicilios ---")
        print("1. Registrar entrega en moto")
        print("2. Registrar entrega en bicicleta")
        print("3. Registrar entrega en carro")
        print("4. Ver entregas")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            destino = input("Destino: ")
            distancia = float(input("Distancia en km: "))

            if opcion == "1":
                entrega = EntregaMoto(destino, distancia)
            elif opcion == "2":
                entrega = EntregaBicicleta(destino, distancia)
            else:
                entrega = EntregaCarro(destino, distancia)

            entregas.append(entrega)
            print("Entrega registrada.")

        elif opcion == "4":
            if not entregas:
                print("No hay entregas registradas.")
            for entrega in entregas:
                print(f"\nTipo: {entrega.__class__.__name__}")
                print(f"Destino: {entrega.destino}")
                print(f"Repartidor: {entrega.asignar_repartidor()}")
                print(f"Tiempo: {entrega.calcular_tiempo()} minutos")

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
