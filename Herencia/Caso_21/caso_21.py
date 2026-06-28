from abc import ABC, abstractmethod


class ProcesoJudicial(ABC):
    @abstractmethod
    def iniciar_proceso(self):
        pass

    @abstractmethod
    def cerrar_proceso(self):
        pass


class CasoCivil(ProcesoJudicial):
    def iniciar_proceso(self):
        return "Caso civil iniciado con radicacion de demanda."

    def cerrar_proceso(self):
        return "Caso civil cerrado con sentencia o acuerdo."


class CasoPenal(ProcesoJudicial):
    def iniciar_proceso(self):
        return "Caso penal iniciado con investigacion formal."

    def cerrar_proceso(self):
        return "Caso penal cerrado con decision judicial."


class CasoLaboral(ProcesoJudicial):
    def iniciar_proceso(self):
        return "Caso laboral iniciado por reclamacion del trabajador."

    def cerrar_proceso(self):
        return "Caso laboral cerrado con conciliacion o fallo."


def ejecutar_proceso(proceso: ProcesoJudicial):
    print(proceso.iniciar_proceso())
    print(proceso.cerrar_proceso())


if __name__ == "__main__":
    procesos = [CasoCivil(), CasoPenal(), CasoLaboral()]
    for proceso in procesos:
        ejecutar_proceso(proceso)
        print("-" * 40)
