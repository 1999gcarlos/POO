from abc import ABC, abstractmethod


class Envio(ABC):
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def estimar_entrega(self):
        pass


class EnvioNacional(Envio):
    def calcular_costo(self):
        return self.peso * 3

    def estimar_entrega(self):
        return "2 a 4 dias"


class EnvioInternacional(Envio):
    def calcular_costo(self):
        return self.peso * 10

    def estimar_entrega(self):
        return "7 a 15 dias"


class EnvioExpress(Envio):
    def calcular_costo(self):
        return self.peso * 6

    def estimar_entrega(self):
        return "24 horas"


def main():
    envios = []

    while True:
        print("\n--- Empresa de mensajeria ---")
        print("1. Registrar envio nacional")
        print("2. Registrar envio internacional")
        print("3. Registrar envio express")
        print("4. Ver envios")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            destino = input("Destino: ")
            peso = float(input("Peso en kg: "))
            if opcion == "1":
                envio = EnvioNacional(destino, peso)
            elif opcion == "2":
                envio = EnvioInternacional(destino, peso)
            else:
                envio = EnvioExpress(destino, peso)
            envios.append(envio)
            print("Envio registrado.")

        elif opcion == "4":
            if not envios:
                print("No hay envios registrados.")
            for envio in envios:
                print(f"{envio.destino}: costo {envio.calcular_costo()}, entrega {envio.estimar_entrega()}")

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
