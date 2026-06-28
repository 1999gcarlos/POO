from abc import ABC, abstractmethod


class Mensaje(ABC):
    @abstractmethod
    def enviar(self):
        pass

    @abstractmethod
    def eliminar(self):
        pass


class MensajeTexto(Mensaje):
    def enviar(self):
        return "Mensaje de texto enviado al destinatario."

    def eliminar(self):
        return "Mensaje de texto eliminado del historial."


class MensajeVoz(Mensaje):
    def enviar(self):
        return "Mensaje de voz enviado con archivo de audio."

    def eliminar(self):
        return "Mensaje de voz eliminado del chat."


class MensajeVideo(Mensaje):
    def enviar(self):
        return "Mensaje de video enviado con contenido multimedia."

    def eliminar(self):
        return "Mensaje de video eliminado de la conversacion."


def ejecutar_proceso(mensaje: Mensaje):
    print(mensaje.enviar())
    print(mensaje.eliminar())


if __name__ == "__main__":
    mensajes = [MensajeTexto(), MensajeVoz(), MensajeVideo()]
    for mensaje in mensajes:
        ejecutar_proceso(mensaje)
        print("-" * 40)
