from abc import ABC, abstractmethod


class Correspondencia(ABC):
    @abstractmethod
    def enviar(self):
        pass

    @abstractmethod
    def rastrear(self):
        pass


class Carta(Correspondencia):
    def enviar(self):
        return "Carta enviada por correo tradicional."

    def rastrear(self):
        return "Carta rastreada con numero de guia basico."


class Paquete(Correspondencia):
    def enviar(self):
        return "Paquete enviado con registro de peso y volumen."

    def rastrear(self):
        return "Paquete rastreado durante el trayecto."


class DocumentoUrgente(Correspondencia):
    def enviar(self):
        return "Documento urgente enviado con prioridad alta."

    def rastrear(self):
        return "Documento urgente rastreado en tiempo real."


def ejecutar_proceso(correspondencia: Correspondencia):
    print(correspondencia.enviar())
    print(correspondencia.rastrear())


if __name__ == "__main__":
    envios = [Carta(), Paquete(), DocumentoUrgente()]
    for envio in envios:
        ejecutar_proceso(envio)
        print("-" * 40)
