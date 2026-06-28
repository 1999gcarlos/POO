# Caso 18 - Plataforma blockchain

## Diagrama UML

```mermaid
classDiagram
    class TransaccionBlockchain {
        <<abstract>>
        +validar()
        +registrar()
    }

    class Bitcoin {
        +validar()
        +registrar()
    }

    class Ethereum {
        +validar()
        +registrar()
    }

    class NFT {
        +validar()
        +registrar()
    }

    TransaccionBlockchain <|-- Bitcoin
    TransaccionBlockchain <|-- Ethereum
    TransaccionBlockchain <|-- NFT
```

## Proceso

```mermaid
flowchart TD
    A["Crear una transaccion blockchain"] --> B{"Seleccionar tipo"}
    B --> C["Bitcoin"]
    B --> D["Ethereum"]
    B --> E["NFT"]
    C --> F["validar()"]
    D --> F
    E --> F
    F --> G["registrar()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`TransaccionBlockchain` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `validar()` y `registrar()`.

Las clases hijas (`Bitcoin`, `Ethereum`, `NFT`) heredan de `TransaccionBlockchain` y pueden especializar esos metodos para representar transacciones con validacion y registro diferentes segun la red. Esto aplica el principio de herencia y permite tratar todos los objetos como `TransaccionBlockchain` sin perder el comportamiento particular de cada tipo.
