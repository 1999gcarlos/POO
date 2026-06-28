from abc import ABC, abstractmethod


class ServicioTelecomunicacion(ABC):
    def __init__(self, cliente, plan):
        self.cliente = cliente
        self.plan = plan

    @abstractmethod
    def activar_servicio(self):
        pass

    @abstractmethod
    def calcular_tarifa(self):
        pass


class Internet(ServicioTelecomunicacion):
    def activar_servicio(self):
        return f"Internet activado para {self.cliente}."

    def calcular_tarifa(self):
        return 80000


class Telefonia(ServicioTelecomunicacion):
    def activar_servicio(self):
        return f"Telefonia activada para {self.cliente}."

    def calcular_tarifa(self):
        return 40000


class Television(ServicioTelecomunicacion):
    def activar_servicio(self):
        return f"Television activada para {self.cliente}."

    def calcular_tarifa(self):
        return 60000


def main():
    servicios = []

    while True:
        print("\n--- Telecomunicaciones ---")
        print("1. Activar internet")
        print("2. Activar telefonia")
        print("3. Activar television")
        print("4. Ver servicios")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            cliente = input("Cliente: ")
            plan = input("Plan: ")
            if opcion == "1":
                servicio = Internet(cliente, plan)
            elif opcion == "2":
                servicio = Telefonia(cliente, plan)
            else:
                servicio = Television(cliente, plan)
            servicios.append(servicio)
            print("Servicio registrado.")

        elif opcion == "4":
            if not servicios:
                print("No hay servicios registrados.")
            for servicio in servicios:
                print(servicio.activar_servicio())
                print(f"Tarifa: {servicio.calcular_tarifa()}")

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
