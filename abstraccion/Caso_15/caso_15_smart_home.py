from abc import ABC, abstractmethod


class DispositivoInteligente(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        self.encendido = False

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass


class Camara(DispositivoInteligente):
    def encender(self):
        self.encendido = True
        return f"Camara {self.nombre} encendida."

    def apagar(self):
        self.encendido = False
        return f"Camara {self.nombre} apagada."


class Bombillo(DispositivoInteligente):
    def encender(self):
        self.encendido = True
        return f"Bombillo {self.nombre} encendido."

    def apagar(self):
        self.encendido = False
        return f"Bombillo {self.nombre} apagado."


class AireAcondicionado(DispositivoInteligente):
    def encender(self):
        self.encendido = True
        return f"Aire acondicionado {self.nombre} encendido."

    def apagar(self):
        self.encendido = False
        return f"Aire acondicionado {self.nombre} apagado."


def main():
    dispositivos = []

    while True:
        print("\n--- Smart Home ---")
        print("1. Registrar camara")
        print("2. Registrar bombillo")
        print("3. Registrar aire acondicionado")
        print("4. Encender y apagar dispositivos")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            nombre = input("Nombre del dispositivo: ")
            if opcion == "1":
                dispositivo = Camara(nombre)
            elif opcion == "2":
                dispositivo = Bombillo(nombre)
            else:
                dispositivo = AireAcondicionado(nombre)
            dispositivos.append(dispositivo)
            print("Dispositivo registrado.")

        elif opcion == "4":
            if not dispositivos:
                print("No hay dispositivos registrados.")
            for dispositivo in dispositivos:
                print(dispositivo.encender())
                print(dispositivo.apagar())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
