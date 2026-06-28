from abc import ABC, abstractmethod


class Contenido(ABC):
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

    @abstractmethod
    def reproducir(self):
        pass

    @abstractmethod
    def pausar(self):
        pass


class Pelicula(Contenido):
    def reproducir(self):
        return f"Reproduciendo pelicula: {self.titulo}"

    def pausar(self):
        return f"Pelicula pausada: {self.titulo}"


class Serie(Contenido):
    def reproducir(self):
        return f"Reproduciendo serie: {self.titulo}"

    def pausar(self):
        return f"Serie pausada: {self.titulo}"


class Documental(Contenido):
    def reproducir(self):
        return f"Reproduciendo documental: {self.titulo}"

    def pausar(self):
        return f"Documental pausado: {self.titulo}"


def main():
    contenidos = []

    while True:
        print("\n--- Plataforma de streaming ---")
        print("1. Registrar pelicula")
        print("2. Registrar serie")
        print("3. Registrar documental")
        print("4. Reproducir contenido")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            titulo = input("Titulo: ")
            duracion = int(input("Duracion en minutos: "))
            if opcion == "1":
                contenido = Pelicula(titulo, duracion)
            elif opcion == "2":
                contenido = Serie(titulo, duracion)
            else:
                contenido = Documental(titulo, duracion)
            contenidos.append(contenido)
            print("Contenido registrado.")

        elif opcion == "4":
            if not contenidos:
                print("No hay contenido registrado.")
            for contenido in contenidos:
                print(contenido.reproducir())
                print(contenido.pausar())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
