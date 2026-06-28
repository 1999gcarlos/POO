from abc import ABC, abstractmethod


class Entrenamiento(ABC):
    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def finalizar(self):
        pass


class EntrenamientoFutbol(Entrenamiento):
    def iniciar(self):
        return "Entrenamiento de futbol iniciado con calentamiento."

    def finalizar(self):
        return "Entrenamiento de futbol finalizado con estiramientos."


class EntrenamientoNatacion(Entrenamiento):
    def iniciar(self):
        return "Entrenamiento de natacion iniciado en piscina."

    def finalizar(self):
        return "Entrenamiento de natacion finalizado con registro de tiempos."


class EntrenamientoBoxeo(Entrenamiento):
    def iniciar(self):
        return "Entrenamiento de boxeo iniciado con tecnica de golpes."

    def finalizar(self):
        return "Entrenamiento de boxeo finalizado con recuperacion."


def ejecutar_proceso(entrenamiento: Entrenamiento):
    print(entrenamiento.iniciar())
    print(entrenamiento.finalizar())


if __name__ == "__main__":
    entrenamientos = [
        EntrenamientoFutbol(),
        EntrenamientoNatacion(),
        EntrenamientoBoxeo(),
    ]
    for entrenamiento in entrenamientos:
        ejecutar_proceso(entrenamiento)
        print("-" * 40)
