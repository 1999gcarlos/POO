from abc import ABC, abstractmethod


class DispositivoRed(ABC):
    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = ip

    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def transmitir_datos(self):
        pass


class Router(DispositivoRed):
    def conectar(self):
        return f"Router {self.nombre} conectado en {self.ip}."

    def transmitir_datos(self):
        return "Router enruta paquetes."


class Switch(DispositivoRed):
    def conectar(self):
        return f"Switch {self.nombre} conectado en {self.ip}."

    def transmitir_datos(self):
        return "Switch conmuta datos en la LAN."


class AccessPoint(DispositivoRed):
    def conectar(self):
        return f"Access Point {self.nombre} conectado en {self.ip}."

    def transmitir_datos(self):
        return "Access Point transmite datos por WiFi."


def main():
    dispositivos = []

    while True:
        print("\n--- Sistema de redes ---")
        print("1. Registrar router")
        print("2. Registrar switch")
        print("3. Registrar access point")
        print("4. Conectar dispositivos")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            nombre = input("Nombre: ")
            ip = input("Direccion IP: ")
            if opcion == "1":
                dispositivo = Router(nombre, ip)
            elif opcion == "2":
                dispositivo = Switch(nombre, ip)
            else:
                dispositivo = AccessPoint(nombre, ip)
            dispositivos.append(dispositivo)
            print("Dispositivo registrado.")

        elif opcion == "4":
            if not dispositivos:
                print("No hay dispositivos registrados.")
            for dispositivo in dispositivos:
                print(dispositivo.conectar())
                print(dispositivo.transmitir_datos())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
