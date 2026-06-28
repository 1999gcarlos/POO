from abc import ABC, abstractmethod


class Audio(ABC):
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

    @abstractmethod
    def reproducir(self):
        pass

    @abstractmethod
    def detener(self):
        pass


class Cancion(Audio):
    def reproducir(self):
        return f"Reproduciendo cancion: {self.titulo}"

    def detener(self):
        return f"Cancion detenida: {self.titulo}"


class Podcast(Audio):
    def reproducir(self):
        return f"Reproduciendo podcast: {self.titulo}"

    def detener(self):
        return f"Podcast detenido: {self.titulo}"


class Audiolibro(Audio):
    def reproducir(self):
        return f"Reproduciendo audiolibro: {self.titulo}"

    def detener(self):
        return f"Audiolibro detenido: {self.titulo}"


def main():
    audios = []

    while True:
        print("\n--- Plataforma de musica ---")
        print("1. Registrar cancion")
        print("2. Registrar podcast")
        print("3. Registrar audiolibro")
        print("4. Reproducir audios")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            titulo = input("Titulo: ")
            duracion = int(input("Duracion en minutos: "))
            if opcion == "1":
                audio = Cancion(titulo, duracion)
            elif opcion == "2":
                audio = Podcast(titulo, duracion)
            else:
                audio = Audiolibro(titulo, duracion)
            audios.append(audio)
            print("Audio registrado.")

        elif opcion == "4":
            if not audios:
                print("No hay audios registrados.")
            for audio in audios:
                print(audio.reproducir())
                print(audio.detener())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
