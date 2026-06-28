from abc import ABC, abstractmethod


class Vuelo(ABC):
    def __init__(self, codigo, destino):
        self.codigo = codigo
        self.destino = destino

    @abstractmethod
    def despegar(self):
        pass

    @abstractmethod
    def aterrizar(self):
        pass


class VueloNacional(Vuelo):
    def despegar(self):
        return f"Vuelo nacional {self.codigo} despega hacia {self.destino}."

    def aterrizar(self):
        return f"Vuelo nacional {self.codigo} aterriza."


class VueloInternacional(Vuelo):
    def despegar(self):
        return f"Vuelo internacional {self.codigo} despega hacia {self.destino}."

    def aterrizar(self):
        return f"Vuelo internacional {self.codigo} aterriza."


class VueloCarga(Vuelo):
    def despegar(self):
        return f"Vuelo de carga {self.codigo} despega hacia {self.destino}."

    def aterrizar(self):
        return f"Vuelo de carga {self.codigo} aterriza."


def main():
    vuelos = []

    while True:
        print("\n--- Aeropuerto internacional ---")
        print("1. Programar vuelo nacional")
        print("2. Programar vuelo internacional")
        print("3. Programar vuelo de carga")
        print("4. Operar vuelos")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            codigo = input("Codigo del vuelo: ")
            destino = input("Destino: ")
            if opcion == "1":
                vuelo = VueloNacional(codigo, destino)
            elif opcion == "2":
                vuelo = VueloInternacional(codigo, destino)
            else:
                vuelo = VueloCarga(codigo, destino)
            vuelos.append(vuelo)
            print("Vuelo programado.")

        elif opcion == "4":
            if not vuelos:
                print("No hay vuelos programados.")
            for vuelo in vuelos:
                print(vuelo.despegar())
                print(vuelo.aterrizar())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
