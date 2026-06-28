from abc import ABC, abstractmethod


class Cultivo(ABC):
    @abstractmethod
    def sembrar(self):
        pass

    @abstractmethod
    def cosechar(self):
        pass


class CultivoMaiz(Cultivo):
    def sembrar(self):
        return "Cultivo de maiz sembrado en surcos."

    def cosechar(self):
        return "Cultivo de maiz cosechado cuando la mazorca madura."


class CultivoCafe(Cultivo):
    def sembrar(self):
        return "Cultivo de cafe sembrado en zona de sombra."

    def cosechar(self):
        return "Cultivo de cafe cosechado seleccionando granos maduros."


class CultivoArroz(Cultivo):
    def sembrar(self):
        return "Cultivo de arroz sembrado en terreno humedo."

    def cosechar(self):
        return "Cultivo de arroz cosechado en temporada adecuada."


def ejecutar_proceso(cultivo: Cultivo):
    print(cultivo.sembrar())
    print(cultivo.cosechar())


if __name__ == "__main__":
    cultivos = [CultivoMaiz(), CultivoCafe(), CultivoArroz()]
    for cultivo in cultivos:
        ejecutar_proceso(cultivo)
        print("-" * 40)
