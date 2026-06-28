from abc import ABC, abstractmethod


class Miembro(ABC):
    @abstractmethod
    def ingresar_gimnasio(self):
        pass

    @abstractmethod
    def pagar_mensualidad(self):
        pass


class MiembroBasico(Miembro):
    def ingresar_gimnasio(self):
        return "Miembro basico ingresa al area general del gimnasio."

    def pagar_mensualidad(self):
        return "Miembro basico paga la mensualidad estandar."


class MiembroPremium(Miembro):
    def ingresar_gimnasio(self):
        return "Miembro premium ingresa al gimnasio y a clases grupales."

    def pagar_mensualidad(self):
        return "Miembro premium paga la mensualidad con beneficios adicionales."


class MiembroVIP(Miembro):
    def ingresar_gimnasio(self):
        return "Miembro VIP ingresa a todas las zonas exclusivas del gimnasio."

    def pagar_mensualidad(self):
        return "Miembro VIP paga la mensualidad con servicio personalizado."


def ejecutar_proceso(miembro: Miembro):
    print(miembro.ingresar_gimnasio())
    print(miembro.pagar_mensualidad())


if __name__ == "__main__":
    miembros = [MiembroBasico(), MiembroPremium(), MiembroVIP()]
    for miembro in miembros:
        ejecutar_proceso(miembro)
        print("-" * 40)
