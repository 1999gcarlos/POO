from abc import ABC, abstractmethod


class Camara(ABC):
    @abstractmethod
    def capturar(self):
        pass

    @abstractmethod
    def guardar_imagen(self):
        pass


class CamaraProfesional(Camara):
    def capturar(self):
        return "Camara profesional captura imagen en alta resolucion."

    def guardar_imagen(self):
        return "Camara profesional guarda imagen en formato RAW."


class CamaraSeguridad(Camara):
    def capturar(self):
        return "Camara de seguridad captura video continuo."

    def guardar_imagen(self):
        return "Camara de seguridad guarda evidencia en servidor."


class CamaraDrone(Camara):
    def capturar(self):
        return "Camara drone captura imagen aerea."

    def guardar_imagen(self):
        return "Camara drone guarda imagen con coordenadas."


def ejecutar_proceso(camara: Camara):
    print(camara.capturar())
    print(camara.guardar_imagen())


if __name__ == "__main__":
    camaras = [CamaraProfesional(), CamaraSeguridad(), CamaraDrone()]
    for camara in camaras:
        ejecutar_proceso(camara)
        print("-" * 40)
