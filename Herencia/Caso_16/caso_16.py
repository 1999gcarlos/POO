from abc import ABC, abstractmethod


class Habitacion(ABC):
    @abstractmethod
    def reservar(self):
        pass

    @abstractmethod
    def liberar(self):
        pass


class HabitacionSimple(Habitacion):
    def reservar(self):
        return "Habitacion simple reservada para un huesped."

    def liberar(self):
        return "Habitacion simple liberada y disponible."


class HabitacionDoble(Habitacion):
    def reservar(self):
        return "Habitacion doble reservada para dos huespedes."

    def liberar(self):
        return "Habitacion doble liberada despues de limpieza."


class Suite(Habitacion):
    def reservar(self):
        return "Suite reservada con servicios premium."

    def liberar(self):
        return "Suite liberada y revisada por administracion."


def ejecutar_proceso(habitacion: Habitacion):
    print(habitacion.reservar())
    print(habitacion.liberar())


if __name__ == "__main__":
    habitaciones = [HabitacionSimple(), HabitacionDoble(), Suite()]
    for habitacion in habitaciones:
        ejecutar_proceso(habitacion)
        print("-" * 40)
