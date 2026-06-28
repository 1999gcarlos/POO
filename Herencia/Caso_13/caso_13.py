from abc import ABC, abstractmethod


class EquipoMinero(ABC):
    @abstractmethod
    def operar(self):
        pass

    @abstractmethod
    def apagar(self):
        pass


class Perforadora(EquipoMinero):
    def operar(self):
        return "Perforadora operando para abrir cavidades en roca."

    def apagar(self):
        return "Perforadora apagada con protocolo de seguridad."


class ExcavadoraMineria(EquipoMinero):
    def operar(self):
        return "Excavadora minera operando para mover material."

    def apagar(self):
        return "Excavadora minera apagada y asegurada."


class Trituradora(EquipoMinero):
    def operar(self):
        return "Trituradora operando para reducir rocas."

    def apagar(self):
        return "Trituradora apagada despues de limpiar el sistema."


def ejecutar_proceso(equipo: EquipoMinero):
    print(equipo.operar())
    print(equipo.apagar())


if __name__ == "__main__":
    equipos = [Perforadora(), ExcavadoraMineria(), Trituradora()]
    for equipo in equipos:
        ejecutar_proceso(equipo)
        print("-" * 40)
