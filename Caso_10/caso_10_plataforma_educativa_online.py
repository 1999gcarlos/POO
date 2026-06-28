from abc import ABC, abstractmethod


class Curso(ABC):
    def __init__(self, nombre, estudiante):
        self.nombre = nombre
        self.estudiante = estudiante

    @abstractmethod
    def iniciar_curso(self):
        pass

    @abstractmethod
    def evaluar_estudiante(self):
        pass


class CursoProgramacion(Curso):
    def iniciar_curso(self):
        return f"Iniciando curso de programacion: {self.nombre}"

    def evaluar_estudiante(self):
        return f"Evaluando codigo de {self.estudiante}"


class CursoRedes(Curso):
    def iniciar_curso(self):
        return f"Iniciando curso de redes: {self.nombre}"

    def evaluar_estudiante(self):
        return f"Evaluando configuracion de red de {self.estudiante}"


class CursoBaseDatos(Curso):
    def iniciar_curso(self):
        return f"Iniciando curso de bases de datos: {self.nombre}"

    def evaluar_estudiante(self):
        return f"Evaluando consultas SQL de {self.estudiante}"


def main():
    cursos = []

    while True:
        print("\n--- Plataforma educativa online ---")
        print("1. Registrar curso de programacion")
        print("2. Registrar curso de redes")
        print("3. Registrar curso de bases de datos")
        print("4. Iniciar y evaluar cursos")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            nombre = input("Nombre del curso: ")
            estudiante = input("Nombre del estudiante: ")
            if opcion == "1":
                curso = CursoProgramacion(nombre, estudiante)
            elif opcion == "2":
                curso = CursoRedes(nombre, estudiante)
            else:
                curso = CursoBaseDatos(nombre, estudiante)
            cursos.append(curso)
            print("Curso registrado.")

        elif opcion == "4":
            if not cursos:
                print("No hay cursos registrados.")
            for curso in cursos:
                print(curso.iniciar_curso())
                print(curso.evaluar_estudiante())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
