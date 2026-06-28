from abc import ABC, abstractmethod


class MaterialBiblioteca(ABC):
    @abstractmethod
    def prestar(self):
        pass

    @abstractmethod
    def devolver(self):
        pass


class Libro(MaterialBiblioteca):
    def prestar(self):
        return "Libro prestado por el periodo regular."

    def devolver(self):
        return "Libro devuelto y ubicado en la estanteria."


class Revista(MaterialBiblioteca):
    def prestar(self):
        return "Revista prestada para consulta temporal."

    def devolver(self):
        return "Revista devuelta al area de publicaciones."


class Tesis(MaterialBiblioteca):
    def prestar(self):
        return "Tesis prestada bajo condiciones especiales."

    def devolver(self):
        return "Tesis devuelta al archivo academico."


def ejecutar_proceso(material: MaterialBiblioteca):
    print(material.prestar())
    print(material.devolver())


if __name__ == "__main__":
    materiales = [Libro(), Revista(), Tesis()]
    for material in materiales:
        ejecutar_proceso(material)
        print("-" * 40)
