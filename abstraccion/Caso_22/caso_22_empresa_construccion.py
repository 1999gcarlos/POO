from abc import ABC, abstractmethod


class Maquinaria(ABC):
    def __init__(self, codigo):
        self.codigo = codigo

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def trabajar(self):
        pass


class Excavadora(Maquinaria):
    def encender(self):
        return f"Excavadora {self.codigo} encendida."

    def trabajar(self):
        return "Excavadora removiendo tierra."


class Grua(Maquinaria):
    def encender(self):
        return f"Grua {self.codigo} encendida."

    def trabajar(self):
        return "Grua levantando materiales."


class Mezcladora(Maquinaria):
    def encender(self):
        return f"Mezcladora {self.codigo} encendida."

    def trabajar(self):
        return "Mezcladora preparando concreto."


def main():
    maquinas = []

    while True:
        print("\n--- Empresa de construccion ---")
        print("1. Registrar excavadora")
        print("2. Registrar grua")
        print("3. Registrar mezcladora")
        print("4. Usar maquinaria")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            codigo = input("Codigo de maquinaria: ")
            if opcion == "1":
                maquina = Excavadora(codigo)
            elif opcion == "2":
                maquina = Grua(codigo)
            else:
                maquina = Mezcladora(codigo)
            maquinas.append(maquina)
            print("Maquinaria registrada.")

        elif opcion == "4":
            if not maquinas:
                print("No hay maquinaria registrada.")
            for maquina in maquinas:
                print(maquina.encender())
                print(maquina.trabajar())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
