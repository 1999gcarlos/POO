from abc import ABC, abstractmethod


class EmpleadoHospital(ABC):
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area

    @abstractmethod
    def atender_paciente(self):
        pass

    @abstractmethod
    def generar_reporte(self):
        pass


class Doctor(EmpleadoHospital):
    def atender_paciente(self):
        return f"El doctor {self.nombre} atiende consulta en {self.area}."

    def generar_reporte(self):
        return "Reporte medico general generado."


class Enfermero(EmpleadoHospital):
    def atender_paciente(self):
        return f"El enfermero {self.nombre} toma signos vitales."

    def generar_reporte(self):
        return "Reporte de enfermeria generado."


class Cirujano(EmpleadoHospital):
    def atender_paciente(self):
        return f"El cirujano {self.nombre} prepara una cirugia."

    def generar_reporte(self):
        return "Reporte quirurgico generado."


def main():
    empleados = []

    while True:
        print("\n--- Hospital moderno ---")
        print("1. Registrar doctor")
        print("2. Registrar enfermero")
        print("3. Registrar cirujano")
        print("4. Atender pacientes")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            nombre = input("Nombre: ")
            area = input("Area: ")
            if opcion == "1":
                empleado = Doctor(nombre, area)
            elif opcion == "2":
                empleado = Enfermero(nombre, area)
            else:
                empleado = Cirujano(nombre, area)
            empleados.append(empleado)
            print("Empleado registrado.")

        elif opcion == "4":
            if not empleados:
                print("No hay empleados registrados.")
            for empleado in empleados:
                print(empleado.atender_paciente())
                print(empleado.generar_reporte())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
