from abc import ABC, abstractmethod


class Evaluacion(ABC):
    @abstractmethod
    def calificar(self):
        pass

    @abstractmethod
    def mostrar_resultado(self):
        pass


class Quiz(Evaluacion):
    def calificar(self):
        return "Quiz calificado automaticamente."

    def mostrar_resultado(self):
        return "Resultado del quiz mostrado al estudiante."


class ExamenFinal(Evaluacion):
    def calificar(self):
        return "Examen final calificado con ponderacion alta."

    def mostrar_resultado(self):
        return "Resultado del examen final publicado en plataforma."


class Taller(Evaluacion):
    def calificar(self):
        return "Taller calificado con rubrica de actividades."

    def mostrar_resultado(self):
        return "Resultado del taller mostrado con retroalimentacion."


def ejecutar_proceso(evaluacion: Evaluacion):
    print(evaluacion.calificar())
    print(evaluacion.mostrar_resultado())


if __name__ == "__main__":
    evaluaciones = [Quiz(), ExamenFinal(), Taller()]
    for evaluacion in evaluaciones:
        ejecutar_proceso(evaluacion)
        print("-" * 40)
