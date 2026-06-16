import io
from contextlib import redirect_stdout
from tkinter import END, Button, Entry, Frame, Label, Listbox, StringVar, Tk, messagebox
from tkinter import ttk

from banco_digital import BancoDigital, Cliente, CuentaAhorros, CuentaCorriente


# Este archivo crea una interfaz grafica con Tkinter.
# Importa las clases de banco_digital.py para reutilizar la logica de POO:
# Cliente, BancoDigital, CuentaAhorros y CuentaCorriente.


class InterfazBancoDigital:
    """Ventana principal del banco digital."""

    def __init__(self, ventana: Tk) -> None:
        # La interfaz tambien usa POO: esta clase guarda los elementos
        # de la ventana y define los metodos que responden a los botones.
        self.ventana = ventana
        self.ventana.title("Banco Digital SENA")
        self.ventana.geometry("980x620")

        self.banco = BancoDigital("Banco Digital SENA")
        self.tipo_cuenta = StringVar(value="Ahorros")

        self.crear_componentes()

    def crear_componentes(self) -> None:
        """Crea campos, botones, listas y mensajes de la interfaz."""
        contenedor = Frame(self.ventana, padx=12, pady=12)
        contenedor.pack(fill="both", expand=True)

        panel_superior = Frame(contenedor)
        panel_superior.pack(fill="x")

        self.crear_panel_cliente(panel_superior)
        self.crear_panel_cuenta(panel_superior)
        self.crear_panel_operaciones(panel_superior)

        panel_tablas = Frame(contenedor, pady=10)
        panel_tablas.pack(fill="both", expand=True)

        self.lista_clientes = self.crear_lista(panel_tablas, "Clientes")
        self.lista_cuentas = self.crear_lista(panel_tablas, "Cuentas")

        Label(contenedor, text="Mensajes y resultados:").pack(anchor="w")
        self.salida = Listbox(contenedor, height=10)
        self.salida.pack(fill="both", expand=True)

    def crear_panel_cliente(self, padre: Frame) -> None:
        """Panel para registrar clientes."""
        panel = Frame(padre, padx=8, pady=8, relief="groove", borderwidth=1)
        panel.pack(side="left", fill="both", expand=True, padx=4)

        Label(panel, text="Registrar cliente").pack(anchor="w")
        Label(panel, text="Nombre:").pack(anchor="w")
        self.entrada_nombre = Entry(panel, width=28)
        self.entrada_nombre.pack(fill="x", pady=2)

        Label(panel, text="Documento:").pack(anchor="w")
        self.entrada_documento = Entry(panel, width=28)
        self.entrada_documento.pack(fill="x", pady=2)

        Button(panel, text="Agregar cliente", command=self.registrar_cliente).pack(
            fill="x", pady=6
        )

    def crear_panel_cuenta(self, padre: Frame) -> None:
        """Panel para abrir cuentas bancarias."""
        panel = Frame(padre, padx=8, pady=8, relief="groove", borderwidth=1)
        panel.pack(side="left", fill="both", expand=True, padx=4)

        Label(panel, text="Abrir cuenta").pack(anchor="w")
        Label(panel, text="Numero de cuenta:").pack(anchor="w")
        self.entrada_numero = Entry(panel, width=28)
        self.entrada_numero.pack(fill="x", pady=2)

        Label(panel, text="Saldo inicial:").pack(anchor="w")
        self.entrada_saldo = Entry(panel, width=28)
        self.entrada_saldo.pack(fill="x", pady=2)

        Label(panel, text="Tipo:").pack(anchor="w")
        ttk.Combobox(
            panel,
            textvariable=self.tipo_cuenta,
            values=("Ahorros", "Corriente"),
            state="readonly",
        ).pack(fill="x", pady=2)

        Button(panel, text="Abrir cuenta", command=self.abrir_cuenta).pack(fill="x", pady=6)

    def crear_panel_operaciones(self, padre: Frame) -> None:
        """Panel para depositar, retirar, transferir y aplicar interes."""
        panel = Frame(padre, padx=8, pady=8, relief="groove", borderwidth=1)
        panel.pack(side="left", fill="both", expand=True, padx=4)

        Label(panel, text="Operaciones").pack(anchor="w")
        Label(panel, text="Monto / porcentaje:").pack(anchor="w")
        self.entrada_monto = Entry(panel, width=28)
        self.entrada_monto.pack(fill="x", pady=2)

        Label(panel, text="Cuenta destino para transferencia:").pack(anchor="w")
        self.entrada_destino = Entry(panel, width=28)
        self.entrada_destino.pack(fill="x", pady=2)

        Button(panel, text="Depositar", command=self.depositar).pack(fill="x", pady=2)
        Button(panel, text="Retirar", command=self.retirar).pack(fill="x", pady=2)
        Button(panel, text="Transferir", command=self.transferir).pack(fill="x", pady=2)
        Button(panel, text="Aplicar interes", command=self.aplicar_interes).pack(
            fill="x", pady=2
        )
        Button(panel, text="Ver movimientos", command=self.ver_movimientos).pack(
            fill="x", pady=2
        )
        Button(panel, text="Ver resumen", command=self.ver_resumen).pack(fill="x", pady=2)

    def crear_lista(self, padre: Frame, titulo: str) -> Listbox:
        """Crea una lista visual."""
        marco = Frame(padre, padx=5)
        marco.pack(side="left", fill="both", expand=True)

        Label(marco, text=titulo).pack(anchor="w")
        lista = Listbox(marco)
        lista.pack(fill="both", expand=True)
        return lista

    def registrar_cliente(self) -> None:
        """Crea un objeto Cliente y lo registra en el banco."""
        nombre = self.entrada_nombre.get().strip()
        documento = self.entrada_documento.get().strip()

        if not nombre or not documento:
            messagebox.showwarning("Dato faltante", "Escribe nombre y documento.")
            return

        cliente = Cliente(nombre, documento)
        self.banco.registrar_cliente(cliente)
        self.lista_clientes.insert(END, str(cliente))
        self.mostrar_mensaje(f"Cliente registrado: {cliente}")
        self.entrada_nombre.delete(0, END)
        self.entrada_documento.delete(0, END)

    def abrir_cuenta(self) -> None:
        """Crea una cuenta y la asocia al cliente seleccionado."""
        indice_cliente = self.obtener_indice(self.lista_clientes, "Selecciona un cliente.")
        if indice_cliente is None:
            return

        numero = self.entrada_numero.get().strip()
        if not numero:
            messagebox.showwarning("Dato faltante", "Escribe el numero de cuenta.")
            return

        if self.banco.buscar_cuenta(numero) is not None:
            messagebox.showwarning("Cuenta repetida", "Ya existe una cuenta con ese numero.")
            return

        saldo = self.obtener_numero(self.entrada_saldo, "saldo inicial")
        if saldo is None:
            return

        cliente = self.banco.clientes[indice_cliente]

        try:
            if self.tipo_cuenta.get() == "Ahorros":
                cuenta = CuentaAhorros(numero, cliente, saldo)
            else:
                cuenta = CuentaCorriente(numero, cliente, saldo)
        except ValueError as error:
            messagebox.showwarning("Dato invalido", str(error))
            return

        self.banco.abrir_cuenta(cliente, cuenta)
        self.lista_cuentas.insert(END, self.formatear_cuenta(cuenta))
        self.mostrar_mensaje(f"Cuenta abierta: {cuenta.numero} para {cliente.nombre}")
        self.entrada_numero.delete(0, END)
        self.entrada_saldo.delete(0, END)

    def depositar(self) -> None:
        cuenta = self.obtener_cuenta_seleccionada()
        monto = self.obtener_numero(self.entrada_monto, "monto")

        if cuenta is None or monto is None:
            return

        self.mostrar_bloque(self.capturar_salida(cuenta.depositar, monto))
        self.actualizar_lista_cuentas()

    def retirar(self) -> None:
        cuenta = self.obtener_cuenta_seleccionada()
        monto = self.obtener_numero(self.entrada_monto, "monto")

        if cuenta is None or monto is None:
            return

        self.mostrar_bloque(self.capturar_salida(cuenta.retirar, monto))
        self.actualizar_lista_cuentas()

    def transferir(self) -> None:
        cuenta_origen = self.obtener_cuenta_seleccionada()
        monto = self.obtener_numero(self.entrada_monto, "monto")
        numero_destino = self.entrada_destino.get().strip()

        if cuenta_origen is None or monto is None:
            return

        if not numero_destino:
            messagebox.showwarning("Dato faltante", "Escribe la cuenta destino.")
            return

        cuenta_destino = self.banco.buscar_cuenta(numero_destino)
        if cuenta_destino is None:
            messagebox.showwarning("No encontrada", "No existe la cuenta destino.")
            return

        self.mostrar_bloque(self.capturar_salida(cuenta_origen.transferir, cuenta_destino, monto))
        self.actualizar_lista_cuentas()

    def aplicar_interes(self) -> None:
        cuenta = self.obtener_cuenta_seleccionada()
        porcentaje = self.obtener_numero(self.entrada_monto, "porcentaje")

        if cuenta is None or porcentaje is None:
            return

        if not isinstance(cuenta, CuentaAhorros):
            messagebox.showwarning(
                "Operacion no disponible",
                "El interes solo se aplica a cuentas de ahorros.",
            )
            return

        self.mostrar_bloque(self.capturar_salida(cuenta.aplicar_interes, porcentaje))
        self.actualizar_lista_cuentas()

    def ver_movimientos(self) -> None:
        cuenta = self.obtener_cuenta_seleccionada()
        if cuenta is None:
            return

        self.mostrar_bloque(self.capturar_salida(cuenta.mostrar_movimientos))

    def ver_resumen(self) -> None:
        self.limpiar_salida()
        self.mostrar_bloque(self.capturar_salida(self.banco.mostrar_resumen))

    def obtener_cuenta_seleccionada(self):
        indice = self.obtener_indice(self.lista_cuentas, "Selecciona una cuenta.")
        if indice is None:
            return None
        return self.banco.cuentas[indice]

    def obtener_indice(self, lista: Listbox, mensaje: str) -> int | None:
        seleccion = lista.curselection()
        if not seleccion:
            messagebox.showwarning("Seleccion requerida", mensaje)
            return None
        return seleccion[0]

    def obtener_numero(self, entrada: Entry, nombre_campo: str) -> float | None:
        valor = entrada.get().strip()
        if not valor:
            messagebox.showwarning("Dato faltante", f"Escribe el {nombre_campo}.")
            return None

        try:
            return float(valor)
        except ValueError:
            messagebox.showwarning("Dato invalido", f"El {nombre_campo} debe ser numerico.")
            return None

    def actualizar_lista_cuentas(self) -> None:
        self.lista_cuentas.delete(0, END)
        for cuenta in self.banco.cuentas:
            self.lista_cuentas.insert(END, self.formatear_cuenta(cuenta))

    def formatear_cuenta(self, cuenta) -> str:
        return (
            f"{cuenta.numero} | {cuenta.obtener_tipo()} | "
            f"{cuenta.titular.nombre} | ${cuenta.saldo:.2f}"
        )

    def capturar_salida(self, funcion, *args) -> str:
        """Convierte los print() del modelo en texto para mostrarlo en la interfaz."""
        salida_temporal = io.StringIO()
        with redirect_stdout(salida_temporal):
            funcion(*args)
        return salida_temporal.getvalue().strip()

    def mostrar_mensaje(self, mensaje: str) -> None:
        self.salida.insert(END, mensaje)
        self.salida.see(END)

    def mostrar_bloque(self, texto: str) -> None:
        for linea in texto.splitlines():
            self.mostrar_mensaje(linea)

    def limpiar_salida(self) -> None:
        self.salida.delete(0, END)


def main() -> None:
    ventana = Tk()
    InterfazBancoDigital(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
