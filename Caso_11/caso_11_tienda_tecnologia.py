from abc import ABC, abstractmethod


class ProductoTecnologico(ABC):
    def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio

    @abstractmethod
    def calcular_descuento(self):
        pass

    @abstractmethod
    def mostrar_informacion(self):
        pass


class Laptop(ProductoTecnologico):
    def calcular_descuento(self):
        return self.precio * 0.10

    def mostrar_informacion(self):
        return f"Laptop {self.marca}. Precio final: {self.precio - self.calcular_descuento()}"


class Celular(ProductoTecnologico):
    def calcular_descuento(self):
        return self.precio * 0.08

    def mostrar_informacion(self):
        return f"Celular {self.marca}. Precio final: {self.precio - self.calcular_descuento()}"


class Tablet(ProductoTecnologico):
    def calcular_descuento(self):
        return self.precio * 0.05

    def mostrar_informacion(self):
        return f"Tablet {self.marca}. Precio final: {self.precio - self.calcular_descuento()}"


def main():
    productos = []

    while True:
        print("\n--- Tienda de tecnologia ---")
        print("1. Registrar laptop")
        print("2. Registrar celular")
        print("3. Registrar tablet")
        print("4. Ver productos")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            marca = input("Marca: ")
            precio = float(input("Precio: "))
            if opcion == "1":
                producto = Laptop(marca, precio)
            elif opcion == "2":
                producto = Celular(marca, precio)
            else:
                producto = Tablet(marca, precio)
            productos.append(producto)
            print("Producto registrado.")

        elif opcion == "4":
            if not productos:
                print("No hay productos registrados.")
            for producto in productos:
                print(producto.mostrar_informacion())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
