from abc import ABC, abstractmethod


class TransaccionBlockchain(ABC):
    @abstractmethod
    def validar(self):
        pass

    @abstractmethod
    def registrar(self):
        pass


class Bitcoin(TransaccionBlockchain):
    def validar(self):
        return "Transaccion Bitcoin validada por la red."

    def registrar(self):
        return "Transaccion Bitcoin registrada en la cadena."


class Ethereum(TransaccionBlockchain):
    def validar(self):
        return "Transaccion Ethereum validada con contrato inteligente."

    def registrar(self):
        return "Transaccion Ethereum registrada en blockchain."


class NFT(TransaccionBlockchain):
    def validar(self):
        return "Transaccion NFT validada por propiedad digital."

    def registrar(self):
        return "Transaccion NFT registrada con token unico."


def ejecutar_proceso(transaccion: TransaccionBlockchain):
    print(transaccion.validar())
    print(transaccion.registrar())


if __name__ == "__main__":
    transacciones = [Bitcoin(), Ethereum(), NFT()]
    for transaccion in transacciones:
        ejecutar_proceso(transaccion)
        print("-" * 40)
