from abc import ABC, abstractmethod


class ConsultaMedica(ABC):
    def __init__(self, paciente):
        self.paciente = paciente

    @abstractmethod
    def diagnosticar(self):
        pass

    @abstractmethod
    def generar_formula(self):
        pass


class ConsultaGeneral(ConsultaMedica):
    def diagnosticar(self):
        return f"Diagnostico general para {self.paciente}."

    def generar_formula(self):
        return "Formula de medicina general generada."


class ConsultaOdontologia(ConsultaMedica):
    def diagnosticar(self):
        return f"Diagnostico odontologico para {self.paciente}."

    def generar_formula(self):
        return "Formula odontologica generada."


class ConsultaPsicologia(ConsultaMedica):
    def diagnosticar(self):
        return f"Diagnostico psicologico para {self.paciente}."

    def generar_formula(self):
        return "Recomendaciones psicologicas generadas."


def main():
    consultas = []

    while True:
        print("\n--- Plataforma de salud ---")
        print("1. Registrar consulta general")
        print("2. Registrar consulta de odontologia")
        print("3. Registrar consulta de psicologia")
        print("4. Atender consultas")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            paciente = input("Paciente: ")
            if opcion == "1":
                consulta = ConsultaGeneral(paciente)
            elif opcion == "2":
                consulta = ConsultaOdontologia(paciente)
            else:
                consulta = ConsultaPsicologia(paciente)
            consultas.append(consulta)
            print("Consulta registrada.")

        elif opcion == "4":
            if not consultas:
                print("No hay consultas registradas.")
            for consulta in consultas:
                print(consulta.diagnosticar())
                print(consulta.generar_formula())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
