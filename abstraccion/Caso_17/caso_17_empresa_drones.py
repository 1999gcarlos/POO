from abc import ABC, abstractmethod


class Drone(ABC):
    def __init__(self, codigo):
        self.codigo = codigo

    @abstractmethod
    def despegar(self):
        pass

    @abstractmethod
    def aterrizar(self):
        pass


class DroneEntrega(Drone):
    def despegar(self):
        return f"Drone de entrega {self.codigo} despega con paquete."

    def aterrizar(self):
        return f"Drone de entrega {self.codigo} aterriza."


class DroneMilitar(Drone):
    def despegar(self):
        return f"Drone militar {self.codigo} despega para mision."

    def aterrizar(self):
        return f"Drone militar {self.codigo} aterriza."


class DroneFotografia(Drone):
    def despegar(self):
        return f"Drone fotografico {self.codigo} despega para captura."

    def aterrizar(self):
        return f"Drone fotografico {self.codigo} aterriza."


def main():
    drones = []

    while True:
        print("\n--- Empresa de drones ---")
        print("1. Registrar drone de entrega")
        print("2. Registrar drone militar")
        print("3. Registrar drone de fotografia")
        print("4. Ejecutar vuelo")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            codigo = input("Codigo del drone: ")
            if opcion == "1":
                drone = DroneEntrega(codigo)
            elif opcion == "2":
                drone = DroneMilitar(codigo)
            else:
                drone = DroneFotografia(codigo)
            drones.append(drone)
            print("Drone registrado.")

        elif opcion == "4":
            if not drones:
                print("No hay drones registrados.")
            for drone in drones:
                print(drone.despegar())
                print(drone.aterrizar())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
