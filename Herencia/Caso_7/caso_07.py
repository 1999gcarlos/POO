from abc import ABC, abstractmethod


class Evento(ABC):
    @abstractmethod
    def iniciar_evento(self):
        pass

    @abstractmethod
    def finalizar_evento(self):
        pass


class Concierto(Evento):
    def iniciar_evento(self):
        return "Concierto iniciado con apertura de escenario."

    def finalizar_evento(self):
        return "Concierto finalizado con cierre tecnico."


class Conferencia(Evento):
    def iniciar_evento(self):
        return "Conferencia iniciada con registro de asistentes."

    def finalizar_evento(self):
        return "Conferencia finalizada con entrega de memorias."


class FiestaPrivada(Evento):
    def iniciar_evento(self):
        return "Fiesta privada iniciada con control de invitados."

    def finalizar_evento(self):
        return "Fiesta privada finalizada con cierre del salon."


def ejecutar_proceso(evento: Evento):
    print(evento.iniciar_evento())
    print(evento.finalizar_evento())


if __name__ == "__main__":
    eventos = [Concierto(), Conferencia(), FiestaPrivada()]
    for evento in eventos:
        ejecutar_proceso(evento)
        print("-" * 40)
