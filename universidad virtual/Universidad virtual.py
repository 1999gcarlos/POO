from abc import ABC, abstractmethod


# POO significa Programacion Orientada a Objetos.
# En este paradigma se representan elementos del mundo real como "objetos".
# Cada objeto tiene:
# - Atributos: datos o caracteristicas, por ejemplo nombre y correo.
# - Metodos: acciones que puede realizar, por ejemplo iniciar_sesion().


class Usuario(ABC):
    """Clase base abstracta para cualquier usuario de la universidad virtual."""

    # Una clase abstracta sirve como plantilla general.
    # No se deberia crear un Usuario generico, sino usuarios concretos
    # como Estudiante o Profesor.

    def __init__(self, nombre: str, correo: str) -> None:
        # Encapsulamiento: los datos del objeto se guardan dentro de self.
        # self representa al objeto actual que se esta creando o usando.
        self.nombre = nombre
        self.correo = correo

    def iniciar_sesion(self) -> None:
        """Simula el inicio de sesion del usuario."""
        print(f"{self.nombre} ha iniciado sesion.")

    @abstractmethod
    def mostrar_permisos(self) -> None:
        """Cada tipo de usuario debe definir sus propios permisos."""
        # Abstraccion: obligamos a las clases hijas a implementar este metodo.
        # Asi todos los usuarios tienen mostrar_permisos(), pero cada uno
        # lo adapta a su propio rol.
        pass


class Estudiante(Usuario):
    """Usuario que puede ver cursos, realizar actividades y consultar notas."""

    # Herencia: Estudiante reutiliza atributos y metodos de Usuario.
    def __init__(self, nombre: str, correo: str, carrera: str) -> None:
        # super() llama al constructor de la clase padre Usuario.
        super().__init__(nombre, correo)
        self.carrera = carrera

    def mostrar_permisos(self) -> None:
        # Polimorfismo: este metodo existe en Usuario, Estudiante y Profesor,
        # pero se comporta diferente segun el tipo de objeto.
        print("Permisos del estudiante:")
        print("- Ver cursos")
        print("- Realizar actividades")
        print("- Consultar calificaciones")

    def __str__(self) -> str:
        return f"{self.nombre} - Estudiante de {self.carrera}"


class Profesor(Usuario):
    """Usuario que puede crear cursos, calificar y gestionar actividades."""

    def __init__(self, nombre: str, correo: str, especialidad: str) -> None:
        super().__init__(nombre, correo)
        self.especialidad = especialidad

    def mostrar_permisos(self) -> None:
        print("Permisos del profesor:")
        print("- Crear cursos")
        print("- Calificar estudiantes")
        print("- Gestionar actividades")

    def __str__(self) -> str:
        return f"{self.nombre} - Profesor de {self.especialidad}"


class Curso:
    """Representa un curso de la universidad virtual."""

    def __init__(self, nombre: str, profesor: Profesor) -> None:
        self.nombre = nombre
        # Composicion/asociacion: un Curso contiene o se relaciona con
        # otros objetos, como un Profesor y varios Estudiantes.
        self.profesor = profesor
        self.estudiantes: list[Estudiante] = []

    def inscribir_estudiante(self, estudiante: Estudiante) -> bool:
        """Inscribe un estudiante si aun no esta en el curso."""
        if estudiante in self.estudiantes:
            print(f"{estudiante.nombre} ya esta inscrito en {self.nombre}.")
            return False

        self.estudiantes.append(estudiante)
        print(f"{estudiante.nombre} fue inscrito en {self.nombre}.")
        return True

    def mostrar_info(self) -> None:
        """Muestra la informacion principal del curso."""
        print(f"\nCurso: {self.nombre}")
        print(f"Profesor: {self.profesor.nombre}")
        print("Estudiantes inscritos:")

        if not self.estudiantes:
            print("- No hay estudiantes inscritos")
            return

        for estudiante in self.estudiantes:
            print(f"- {estudiante.nombre}")


class UniversidadVirtual:
    """Administra usuarios y cursos de una universidad virtual."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.usuarios: list[Usuario] = []
        self.cursos: list[Curso] = []

    def agregar_usuario(self, usuario: Usuario) -> None:
        self.usuarios.append(usuario)

    def agregar_curso(self, curso: Curso) -> None:
        self.cursos.append(curso)

    def mostrar_datos(self) -> None:
        """Muestra usuarios registrados y cursos disponibles."""
        print(f"\n=== {self.nombre} ===")

        print("\nUsuarios registrados:")
        for usuario in self.usuarios:
            print(f"- {usuario}")

        print("\nCursos disponibles:")
        for curso in self.cursos:
            print(f"- {curso.nombre}")


def main() -> None:
    """Punto de entrada del programa."""
    universidad = UniversidadVirtual("Universidad Virtual SENA")

    est1 = Estudiante(
        "Carlos Mario",
        "carlos@dominio.edu.co",
        "Analitica de Datos",
    )

    prof1 = Profesor(
        "Rosa Perez",
        "profesor@dominio.edu.co",
        "Programacion",
    )

    universidad.agregar_usuario(est1)
    universidad.agregar_usuario(prof1)

    curso_python = Curso("Python Orientado a Objetos", prof1)
    curso_python.inscribir_estudiante(est1)
    universidad.agregar_curso(curso_python)

    # Aqui se observa el polimorfismo:
    # ambos objetos pueden iniciar sesion y mostrar permisos, aunque
    # Estudiante y Profesor tengan permisos diferentes.
    est1.iniciar_sesion()
    est1.mostrar_permisos()

    print()

    prof1.iniciar_sesion()
    prof1.mostrar_permisos()

    universidad.mostrar_datos()
    curso_python.mostrar_info()


# Esta condicion evita que el programa se ejecute automaticamente
# si el archivo se importa desde otro modulo.
if __name__ == "__main__":
    main()
