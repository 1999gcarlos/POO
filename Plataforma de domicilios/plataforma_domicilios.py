from abc import ABC, abstractmethod


# POO significa Programacion Orientada a Objetos.
# En POO se crean "clases" como moldes y "objetos" como elementos reales.
# Ejemplo:
# - Clase: EntregaMoto
# - Objeto: EntregaMoto("Barranquilla Norte", 10)
#
# Cada objeto tiene:
# - Atributos: datos del objeto, como destino y distancia.
# - Metodos: acciones del objeto, como calcular_tiempo().


class Entrega(ABC):
    """Clase base abstracta para cualquier tipo de entrega."""

    # Abstraccion:
    # Esta clase define lo que toda entrega debe tener, pero no especifica
    # los detalles exactos de cada transporte. Por eso se marca como abstracta.

    def __init__(self, destino: str, distancia: float) -> None:
        # Encapsulamiento:
        # Los datos destino y distancia quedan guardados dentro del objeto.
        if distancia <= 0:
            raise ValueError("La distancia debe ser mayor que cero.")

        self.destino = destino
        self.distancia = distancia

    @abstractmethod
    def calcular_tiempo(self) -> int:
        """Calcula el tiempo estimado de entrega en minutos."""
        # Este metodo es obligatorio para todas las clases hijas.
        pass

    @abstractmethod
    def asignar_repartidor(self) -> str:
        """Devuelve el repartidor asignado a la entrega."""
        pass

    def mostrar_resumen(self) -> None:
        """Muestra la informacion completa de una entrega."""
        print(f"\nTipo: {self.__class__.__name__}")
        print(f"Destino: {self.destino}")
        print(f"Distancia: {self.distancia} km")
        print(f"Repartidor: {self.asignar_repartidor()}")
        print(f"Tiempo estimado: {self.calcular_tiempo()} minutos")


class EntregaMoto(Entrega):
    """Entrega realizada en moto."""

    # Herencia:
    # EntregaMoto hereda de Entrega, por eso ya tiene destino, distancia
    # y el metodo mostrar_resumen().

    VELOCIDAD_PROMEDIO = 40

    def calcular_tiempo(self) -> int:
        # Polimorfismo:
        # Todas las entregas tienen calcular_tiempo(), pero cada transporte
        # usa una velocidad diferente.
        tiempo = self.distancia / self.VELOCIDAD_PROMEDIO * 60
        return round(tiempo)

    def asignar_repartidor(self) -> str:
        return "Juan - Repartidor en Moto"


class EntregaBicicleta(Entrega):
    """Entrega realizada en bicicleta."""

    VELOCIDAD_PROMEDIO = 15

    def calcular_tiempo(self) -> int:
        tiempo = self.distancia / self.VELOCIDAD_PROMEDIO * 60
        return round(tiempo)

    def asignar_repartidor(self) -> str:
        return "Pedro - Repartidor en Bicicleta"


class EntregaCarro(Entrega):
    """Entrega realizada en carro."""

    VELOCIDAD_PROMEDIO = 30

    def calcular_tiempo(self) -> int:
        tiempo = self.distancia / self.VELOCIDAD_PROMEDIO * 60
        return round(tiempo)

    def asignar_repartidor(self) -> str:
        return "Maria - Repartidora en Carro"


class PlataformaDomicilios:
    """Administra varias entregas de una plataforma de domicilios."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.entregas: list[Entrega] = []

    def registrar_entrega(self, entrega: Entrega) -> None:
        """Agrega una entrega a la plataforma."""
        self.entregas.append(entrega)

    def mostrar_entregas(self) -> None:
        """Muestra todas las entregas registradas."""
        print(f"=== {self.nombre} ===")

        if not self.entregas:
            print("No hay entregas registradas.")
            return

        for entrega in self.entregas:
            # Gracias al polimorfismo, no importa si la entrega es en moto,
            # bicicleta o carro: todas saben calcular tiempo y asignar repartidor.
            entrega.mostrar_resumen()


def main() -> None:
    """Punto de entrada del programa."""
    plataforma = PlataformaDomicilios("Domicilios Rapidos")

    entregas = [
        EntregaMoto("Barranquilla Norte", 10),
        EntregaBicicleta("Centro Historico", 5),
        EntregaCarro("Puerto Colombia", 20),
    ]

    for entrega in entregas:
        plataforma.registrar_entrega(entrega)

    plataforma.mostrar_entregas()


# Esta condicion permite importar las clases desde otro archivo sin ejecutar
# automaticamente el programa principal.
if __name__ == "__main__":
    main()
