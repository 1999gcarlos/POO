from abc import ABC, abstractmethod


class ModeloIA(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def entrenar(self):
        pass

    @abstractmethod
    def predecir(self):
        pass


class Chatbot(ModeloIA):
    def entrenar(self):
        return f"Chatbot {self.nombre} entrenado con conversaciones."

    def predecir(self):
        return "Respuesta generada por chatbot."


class ReconocimientoFacial(ModeloIA):
    def entrenar(self):
        return f"Modelo {self.nombre} entrenado con imagenes."

    def predecir(self):
        return "Rostro reconocido."


class TraductorIA(ModeloIA):
    def entrenar(self):
        return f"Traductor {self.nombre} entrenado con textos."

    def predecir(self):
        return "Texto traducido."


def main():
    modelos = []

    while True:
        print("\n--- Plataforma de IA ---")
        print("1. Registrar chatbot")
        print("2. Registrar reconocimiento facial")
        print("3. Registrar traductor IA")
        print("4. Entrenar y predecir")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            nombre = input("Nombre del modelo: ")
            if opcion == "1":
                modelo = Chatbot(nombre)
            elif opcion == "2":
                modelo = ReconocimientoFacial(nombre)
            else:
                modelo = TraductorIA(nombre)
            modelos.append(modelo)
            print("Modelo registrado.")

        elif opcion == "4":
            if not modelos:
                print("No hay modelos registrados.")
            for modelo in modelos:
                print(modelo.entrenar())
                print(modelo.predecir())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
