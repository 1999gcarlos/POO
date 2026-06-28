from abc import ABC, abstractmethod


class Personaje(ABC):
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def defender(self):
        pass


class Guerrero(Personaje):
    def atacar(self):
        return f"{self.nombre} ataca con espada."

    def defender(self):
        return f"{self.nombre} defiende con escudo."


class Arquero(Personaje):
    def atacar(self):
        return f"{self.nombre} dispara una flecha."

    def defender(self):
        return f"{self.nombre} esquiva el ataque."


class Mago(Personaje):
    def atacar(self):
        return f"{self.nombre} lanza un hechizo."

    def defender(self):
        return f"{self.nombre} crea una barrera magica."


def main():
    personajes = []

    while True:
        print("\n--- Sistema de videojuegos ---")
        print("1. Crear guerrero")
        print("2. Crear arquero")
        print("3. Crear mago")
        print("4. Simular combate")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            nombre = input("Nombre del personaje: ")
            vida = int(input("Vida: "))
            if opcion == "1":
                personaje = Guerrero(nombre, vida)
            elif opcion == "2":
                personaje = Arquero(nombre, vida)
            else:
                personaje = Mago(nombre, vida)
            personajes.append(personaje)
            print("Personaje creado.")

        elif opcion == "4":
            if not personajes:
                print("No hay personajes creados.")
            for personaje in personajes:
                print(personaje.atacar())
                print(personaje.defender())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
