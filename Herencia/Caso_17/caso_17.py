from abc import ABC, abstractmethod


class Campana(ABC):
    @abstractmethod
    def lanzar(self):
        pass

    @abstractmethod
    def medir_resultados(self):
        pass


class CampanaTV(Campana):
    def lanzar(self):
        return "Campana de TV lanzada en horario seleccionado."

    def medir_resultados(self):
        return "Resultados de TV medidos por audiencia."


class CampanaDigital(Campana):
    def lanzar(self):
        return "Campana digital lanzada en redes y buscadores."

    def medir_resultados(self):
        return "Resultados digitales medidos por clics y conversiones."


class CampanaRadio(Campana):
    def lanzar(self):
        return "Campana de radio lanzada en emisoras aliadas."

    def medir_resultados(self):
        return "Resultados de radio medidos por alcance estimado."


def ejecutar_proceso(campana: Campana):
    print(campana.lanzar())
    print(campana.medir_resultados())


if __name__ == "__main__":
    campanas = [CampanaTV(), CampanaDigital(), CampanaRadio()]
    for campana in campanas:
        ejecutar_proceso(campana)
        print("-" * 40)
