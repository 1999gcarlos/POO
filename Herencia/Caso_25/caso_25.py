from abc import ABC, abstractmethod


class ContenidoSocial(ABC):
    @abstractmethod
    def publicar(self):
        pass

    @abstractmethod
    def eliminar(self):
        pass


class Foto(ContenidoSocial):
    def publicar(self):
        return "Foto publicada en el perfil del usuario."

    def eliminar(self):
        return "Foto eliminada de la galeria social."


class Video(ContenidoSocial):
    def publicar(self):
        return "Video publicado con reproduccion multimedia."

    def eliminar(self):
        return "Video eliminado del contenido social."


class Historia(ContenidoSocial):
    def publicar(self):
        return "Historia publicada por tiempo limitado."

    def eliminar(self):
        return "Historia eliminada antes de expirar."


def ejecutar_proceso(contenido: ContenidoSocial):
    print(contenido.publicar())
    print(contenido.eliminar())


if __name__ == "__main__":
    contenidos = [Foto(), Video(), Historia()]
    for contenido in contenidos:
        ejecutar_proceso(contenido)
        print("-" * 40)
