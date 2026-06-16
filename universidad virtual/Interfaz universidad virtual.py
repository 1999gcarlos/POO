import importlib.util
import io
from contextlib import redirect_stdout
from pathlib import Path
from tkinter import END, LEFT, RIGHT, Button, Entry, Frame, Label, Listbox, Tk, messagebox


# Este archivo crea una interfaz grafica usando Tkinter.
# Importa las clases del archivo "Universidad virtual.py" para reutilizar
# la logica de POO ya creada: UniversidadVirtual, Estudiante, Profesor y Curso.


def cargar_modelo():
    """Carga el archivo original aunque su nombre tenga espacios."""
    ruta_modelo = Path(__file__).with_name("Universidad virtual.py")
    spec = importlib.util.spec_from_file_location("universidad_virtual", ruta_modelo)

    if spec is None or spec.loader is None:
        raise ImportError("No se pudo cargar el archivo Universidad virtual.py")

    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


modelo = cargar_modelo()
UniversidadVirtual = modelo.UniversidadVirtual
Estudiante = modelo.Estudiante
Profesor = modelo.Profesor
Curso = modelo.Curso


class InterfazUniversidad:
    """Ventana principal de la aplicacion."""

    def __init__(self, ventana: Tk) -> None:
        # La interfaz tambien usa POO: esta clase agrupa atributos
        # y metodos relacionados con la ventana.
        self.ventana = ventana
        self.ventana.title("Universidad Virtual SENA")
        self.ventana.geometry("860x560")

        self.universidad = UniversidadVirtual("Universidad Virtual SENA")
        self.estudiantes = []
        self.profesores = []

        self.crear_componentes()

    def crear_componentes(self) -> None:
        """Crea los botones, cajas de texto y listas de la ventana."""
        contenedor = Frame(self.ventana, padx=12, pady=12)
        contenedor.pack(fill="both", expand=True)

        formulario = Frame(contenedor)
        formulario.pack(fill="x")

        self.entrada_nombre = self.crear_campo(formulario, "Nombre:", 0, 0)
        self.entrada_correo = self.crear_campo(formulario, "Correo:", 0, 2)
        self.entrada_detalle = self.crear_campo(formulario, "Carrera / especialidad:", 1, 0)
        self.entrada_curso = self.crear_campo(formulario, "Nombre del curso:", 1, 2)

        botones = Frame(contenedor, pady=10)
        botones.pack(fill="x")

        Button(botones, text="Agregar estudiante", command=self.agregar_estudiante).pack(
            side=LEFT, padx=4
        )
        Button(botones, text="Agregar profesor", command=self.agregar_profesor).pack(
            side=LEFT, padx=4
        )
        Button(botones, text="Crear curso", command=self.crear_curso).pack(side=LEFT, padx=4)
        Button(botones, text="Inscribir estudiante", command=self.inscribir_estudiante).pack(
            side=LEFT, padx=4
        )
        Button(botones, text="Ver permisos", command=self.ver_permisos).pack(side=LEFT, padx=4)
        Button(botones, text="Ver resumen", command=self.ver_resumen).pack(side=LEFT, padx=4)

        listas = Frame(contenedor)
        listas.pack(fill="both", expand=True)

        self.lista_estudiantes = self.crear_lista(listas, "Estudiantes")
        self.lista_profesores = self.crear_lista(listas, "Profesores")
        self.lista_cursos = self.crear_lista(listas, "Cursos")

        salida_contenedor = Frame(contenedor)
        salida_contenedor.pack(fill="both", expand=True, pady=(10, 0))

        Label(salida_contenedor, text="Salida del programa:").pack(anchor="w")
        self.salida = Listbox(salida_contenedor, height=8)
        self.salida.pack(fill="both", expand=True)

    def crear_campo(self, padre: Frame, texto: str, fila: int, columna: int) -> Entry:
        """Crea una etiqueta y una caja de texto."""
        Label(padre, text=texto).grid(row=fila, column=columna, sticky="w", padx=4, pady=4)
        entrada = Entry(padre, width=30)
        entrada.grid(row=fila, column=columna + 1, sticky="w", padx=4, pady=4)
        return entrada

    def crear_lista(self, padre: Frame, titulo: str) -> Listbox:
        """Crea una lista visual para mostrar objetos."""
        marco = Frame(padre, padx=5)
        marco.pack(side=LEFT, fill="both", expand=True)

        Label(marco, text=titulo).pack(anchor="w")
        lista = Listbox(marco)
        lista.pack(fill="both", expand=True)
        return lista

    def obtener_texto(self, entrada: Entry, nombre_campo: str) -> str | None:
        """Valida que una caja de texto no este vacia."""
        valor = entrada.get().strip()
        if not valor:
            messagebox.showwarning("Dato faltante", f"Escribe el campo: {nombre_campo}")
            return None
        return valor

    def agregar_estudiante(self) -> None:
        nombre = self.obtener_texto(self.entrada_nombre, "Nombre")
        correo = self.obtener_texto(self.entrada_correo, "Correo")
        carrera = self.obtener_texto(self.entrada_detalle, "Carrera")

        if nombre is None or correo is None or carrera is None:
            return

        estudiante = Estudiante(nombre, correo, carrera)
        self.estudiantes.append(estudiante)
        self.universidad.agregar_usuario(estudiante)
        self.lista_estudiantes.insert(END, str(estudiante))
        self.mostrar_linea(f"Estudiante agregado: {estudiante}")

    def agregar_profesor(self) -> None:
        nombre = self.obtener_texto(self.entrada_nombre, "Nombre")
        correo = self.obtener_texto(self.entrada_correo, "Correo")
        especialidad = self.obtener_texto(self.entrada_detalle, "Especialidad")

        if nombre is None or correo is None or especialidad is None:
            return

        profesor = Profesor(nombre, correo, especialidad)
        self.profesores.append(profesor)
        self.universidad.agregar_usuario(profesor)
        self.lista_profesores.insert(END, str(profesor))
        self.mostrar_linea(f"Profesor agregado: {profesor}")

    def crear_curso(self) -> None:
        nombre_curso = self.obtener_texto(self.entrada_curso, "Nombre del curso")
        indice_profesor = self.obtener_indice(self.lista_profesores, "Selecciona un profesor")

        if nombre_curso is None or indice_profesor is None:
            return

        profesor = self.profesores[indice_profesor]
        curso = Curso(nombre_curso, profesor)
        self.universidad.agregar_curso(curso)
        self.lista_cursos.insert(END, curso.nombre)
        self.mostrar_linea(f"Curso creado: {curso.nombre} con {profesor.nombre}")

    def inscribir_estudiante(self) -> None:
        indice_estudiante = self.obtener_indice(
            self.lista_estudiantes, "Selecciona un estudiante"
        )
        indice_curso = self.obtener_indice(self.lista_cursos, "Selecciona un curso")

        if indice_estudiante is None or indice_curso is None:
            return

        estudiante = self.estudiantes[indice_estudiante]
        curso = self.universidad.cursos[indice_curso]
        mensaje = self.capturar_salida(curso.inscribir_estudiante, estudiante)
        self.mostrar_linea(mensaje)

    def ver_permisos(self) -> None:
        """Muestra permisos del usuario seleccionado."""
        indice_estudiante = self.obtener_indice_sin_alerta(self.lista_estudiantes)
        indice_profesor = self.obtener_indice_sin_alerta(self.lista_profesores)

        if indice_estudiante is not None:
            usuario = self.estudiantes[indice_estudiante]
        elif indice_profesor is not None:
            usuario = self.profesores[indice_profesor]
        else:
            messagebox.showwarning(
                "Seleccion requerida",
                "Selecciona un estudiante o un profesor para ver sus permisos.",
            )
            return

        self.mostrar_bloque(self.capturar_salida(usuario.mostrar_permisos))

    def ver_resumen(self) -> None:
        """Muestra datos generales de la universidad y sus cursos."""
        self.salida.delete(0, END)
        self.mostrar_bloque(self.capturar_salida(self.universidad.mostrar_datos))

        for curso in self.universidad.cursos:
            self.mostrar_bloque(self.capturar_salida(curso.mostrar_info))

    def obtener_indice(self, lista: Listbox, mensaje: str) -> int | None:
        seleccion = self.obtener_indice_sin_alerta(lista)
        if seleccion is None:
            messagebox.showwarning("Seleccion requerida", mensaje)
        return seleccion

    def obtener_indice_sin_alerta(self, lista: Listbox) -> int | None:
        seleccion = lista.curselection()
        if not seleccion:
            return None
        return seleccion[0]

    def capturar_salida(self, funcion, *args) -> str:
        """Convierte los print() del modelo en texto para mostrarlo en la interfaz."""
        salida_temporal = io.StringIO()
        with redirect_stdout(salida_temporal):
            funcion(*args)
        return salida_temporal.getvalue().strip()

    def mostrar_linea(self, texto: str) -> None:
        if texto:
            self.salida.insert(END, texto)
            self.salida.see(END)

    def mostrar_bloque(self, texto: str) -> None:
        for linea in texto.splitlines():
            self.mostrar_linea(linea)


def main() -> None:
    ventana = Tk()
    InterfazUniversidad(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
