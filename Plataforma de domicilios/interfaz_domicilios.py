from tkinter import END, Button, Entry, Frame, Label, Listbox, StringVar, Tk, messagebox
from tkinter import ttk

from plataforma_domicilios import (
    EntregaBicicleta,
    EntregaCarro,
    EntregaMoto,
    PlataformaDomicilios,
)


# Este archivo crea una interfaz grafica para la plataforma de domicilios.
# Importa las clases del archivo plataforma_domicilios.py para reutilizar
# la logica creada con Programacion Orientada a Objetos.


class InterfazDomicilios:
    """Ventana principal de la aplicacion de domicilios."""

    def __init__(self, ventana: Tk) -> None:
        # Esta clase tambien aplica POO: agrupa los datos de la ventana
        # y las acciones que puede realizar la interfaz.
        self.ventana = ventana
        self.ventana.title("Plataforma de Domicilios")
        self.ventana.geometry("760x520")

        self.plataforma = PlataformaDomicilios("Domicilios Rapidos")
        self.tipo_entrega = StringVar(value="Moto")

        self.crear_componentes()

    def crear_componentes(self) -> None:
        """Crea los campos, botones y listas de la interfaz."""
        contenedor = Frame(self.ventana, padx=12, pady=12)
        contenedor.pack(fill="both", expand=True)

        formulario = Frame(contenedor)
        formulario.pack(fill="x")

        Label(formulario, text="Destino:").grid(row=0, column=0, sticky="w", padx=4, pady=4)
        self.entrada_destino = Entry(formulario, width=35)
        self.entrada_destino.grid(row=0, column=1, sticky="w", padx=4, pady=4)

        Label(formulario, text="Distancia en km:").grid(
            row=1, column=0, sticky="w", padx=4, pady=4
        )
        self.entrada_distancia = Entry(formulario, width=35)
        self.entrada_distancia.grid(row=1, column=1, sticky="w", padx=4, pady=4)

        Label(formulario, text="Tipo de entrega:").grid(
            row=2, column=0, sticky="w", padx=4, pady=4
        )
        selector_tipo = ttk.Combobox(
            formulario,
            textvariable=self.tipo_entrega,
            values=("Moto", "Bicicleta", "Carro"),
            state="readonly",
            width=32,
        )
        selector_tipo.grid(row=2, column=1, sticky="w", padx=4, pady=4)

        botones = Frame(contenedor, pady=10)
        botones.pack(fill="x")

        Button(botones, text="Registrar entrega", command=self.registrar_entrega).pack(
            side="left", padx=4
        )
        Button(botones, text="Ver entregas", command=self.ver_entregas).pack(
            side="left", padx=4
        )
        Button(botones, text="Limpiar salida", command=self.limpiar_salida).pack(
            side="left", padx=4
        )

        tabla_contenedor = Frame(contenedor)
        tabla_contenedor.pack(fill="both", expand=True)

        columnas = ("tipo", "destino", "distancia", "repartidor", "tiempo")
        self.tabla = ttk.Treeview(tabla_contenedor, columns=columnas, show="headings")
        self.tabla.heading("tipo", text="Tipo")
        self.tabla.heading("destino", text="Destino")
        self.tabla.heading("distancia", text="Distancia")
        self.tabla.heading("repartidor", text="Repartidor")
        self.tabla.heading("tiempo", text="Tiempo")

        self.tabla.column("tipo", width=110)
        self.tabla.column("destino", width=170)
        self.tabla.column("distancia", width=90)
        self.tabla.column("repartidor", width=210)
        self.tabla.column("tiempo", width=90)
        self.tabla.pack(fill="both", expand=True)

        Label(contenedor, text="Mensajes:").pack(anchor="w", pady=(10, 0))
        self.salida = Listbox(contenedor, height=6)
        self.salida.pack(fill="both", expand=True)

    def registrar_entrega(self) -> None:
        """Crea una entrega segun el tipo seleccionado y la guarda."""
        destino = self.entrada_destino.get().strip()
        distancia_texto = self.entrada_distancia.get().strip()

        if not destino:
            messagebox.showwarning("Dato faltante", "Escribe el destino de la entrega.")
            return

        try:
            distancia = float(distancia_texto)
        except ValueError:
            messagebox.showwarning("Dato invalido", "La distancia debe ser un numero.")
            return

        try:
            entrega = self.crear_entrega(destino, distancia)
        except ValueError as error:
            messagebox.showwarning("Dato invalido", str(error))
            return

        self.plataforma.registrar_entrega(entrega)
        self.agregar_entrega_a_tabla(entrega)
        self.mostrar_mensaje(f"Entrega registrada para {destino}.")
        self.limpiar_campos()

    def crear_entrega(self, destino: str, distancia: float):
        """Aplica polimorfismo creando el objeto adecuado segun el transporte."""
        tipo = self.tipo_entrega.get()

        if tipo == "Moto":
            return EntregaMoto(destino, distancia)
        if tipo == "Bicicleta":
            return EntregaBicicleta(destino, distancia)
        if tipo == "Carro":
            return EntregaCarro(destino, distancia)

        raise ValueError("Tipo de entrega no valido.")

    def agregar_entrega_a_tabla(self, entrega) -> None:
        """Muestra una entrega en la tabla."""
        self.tabla.insert(
            "",
            END,
            values=(
                entrega.__class__.__name__,
                entrega.destino,
                f"{entrega.distancia} km",
                entrega.asignar_repartidor(),
                f"{entrega.calcular_tiempo()} min",
            ),
        )

    def ver_entregas(self) -> None:
        """Muestra un resumen textual de las entregas registradas."""
        self.limpiar_salida()

        if not self.plataforma.entregas:
            self.mostrar_mensaje("No hay entregas registradas.")
            return

        self.mostrar_mensaje(f"=== {self.plataforma.nombre} ===")
        for entrega in self.plataforma.entregas:
            self.mostrar_mensaje(
                f"{entrega.__class__.__name__}: {entrega.destino} - "
                f"{entrega.calcular_tiempo()} minutos"
            )

    def limpiar_campos(self) -> None:
        self.entrada_destino.delete(0, END)
        self.entrada_distancia.delete(0, END)
        self.tipo_entrega.set("Moto")

    def limpiar_salida(self) -> None:
        self.salida.delete(0, END)

    def mostrar_mensaje(self, mensaje: str) -> None:
        self.salida.insert(END, mensaje)
        self.salida.see(END)


def main() -> None:
    ventana = Tk()
    InterfazDomicilios(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
