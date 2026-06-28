from abc import ABC, abstractmethod


class Mascota(ABC):
    @abstractmethod
    def vacunar(self):
        pass

    @abstractmethod
    def alimentar(self):
        pass


class Perro(Mascota):
    def vacunar(self):
        return "Perro vacunado segun calendario canino."

    def alimentar(self):
        return "Perro alimentado con concentrado canino."


class Gato(Mascota):
    def vacunar(self):
        return "Gato vacunado segun calendario felino."

    def alimentar(self):
        return "Gato alimentado con comida felina."


class Conejo(Mascota):
    def vacunar(self):
        return "Conejo vacunado con control veterinario."

    def alimentar(self):
        return "Conejo alimentado con heno y vegetales."


def ejecutar_proceso(mascota: Mascota):
    print(mascota.vacunar())
    print(mascota.alimentar())


if __name__ == "__main__":
    mascotas = [Perro(), Gato(), Conejo()]
    for mascota in mascotas:
        ejecutar_proceso(mascota)
        print("-" * 40)
