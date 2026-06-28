from abc import ABC, abstractmethod


class FuenteEnergia(ABC):
    @abstractmethod
    def generar_energia(self):
        pass

    @abstractmethod
    def medir_consumo(self):
        pass


class EnergiaSolar(FuenteEnergia):
    def generar_energia(self):
        return "Energia solar generada mediante paneles fotovoltaicos."

    def medir_consumo(self):
        return "Consumo solar medido en kilovatios hora."


class EnergiaEolica(FuenteEnergia):
    def generar_energia(self):
        return "Energia eolica generada mediante turbinas."

    def medir_consumo(self):
        return "Consumo eolico medido segun produccion del viento."


class EnergiaHidraulica(FuenteEnergia):
    def generar_energia(self):
        return "Energia hidraulica generada por flujo de agua."

    def medir_consumo(self):
        return "Consumo hidraulico medido en la central."


def ejecutar_proceso(fuente: FuenteEnergia):
    print(fuente.generar_energia())
    print(fuente.medir_consumo())


if __name__ == "__main__":
    fuentes = [EnergiaSolar(), EnergiaEolica(), EnergiaHidraulica()]
    for fuente in fuentes:
        ejecutar_proceso(fuente)
        print("-" * 40)
