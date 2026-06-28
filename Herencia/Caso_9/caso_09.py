from abc import ABC, abstractmethod


class Publicacion(ABC):
    @abstractmethod
    def publicar(self):
        pass

    @abstractmethod
    def editar(self):
        pass


class Noticia(Publicacion):
    def publicar(self):
        return "Noticia publicada en la portada del portal."

    def editar(self):
        return "Noticia editada con actualizacion de ultima hora."


class Articulo(Publicacion):
    def publicar(self):
        return "Articulo publicado en la seccion editorial."

    def editar(self):
        return "Articulo editado con revision de contenido."


class Entrevista(Publicacion):
    def publicar(self):
        return "Entrevista publicada con preguntas y respuestas."

    def editar(self):
        return "Entrevista editada para mejorar claridad."


def ejecutar_proceso(publicacion: Publicacion):
    print(publicacion.publicar())
    print(publicacion.editar())


if __name__ == "__main__":
    publicaciones = [Noticia(), Articulo(), Entrevista()]
    for publicacion in publicaciones:
        ejecutar_proceso(publicacion)
        print("-" * 40)
