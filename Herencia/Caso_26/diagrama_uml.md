# Caso 26 - Empresa de reciclaje

## Diagrama UML

```mermaid
classDiagram
    class Residuo {
        <<abstract>>
        +clasificar()
        +reciclar()
    }

    class Plastico {
        +clasificar()
        +reciclar()
    }

    class Vidrio {
        +clasificar()
        +reciclar()
    }

    class Papel {
        +clasificar()
        +reciclar()
    }

    Residuo <|-- Plastico
    Residuo <|-- Vidrio
    Residuo <|-- Papel
```

## Proceso

```mermaid
flowchart TD
    A["Crear un residuo"] --> B{"Seleccionar tipo"}
    B --> C["Plastico"]
    B --> D["Vidrio"]
    B --> E["Papel"]
    C --> F["clasificar()"]
    D --> F
    E --> F
    F --> G["reciclar()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Residuo` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `clasificar()` y `reciclar()`.

Las clases hijas (`Plastico`, `Vidrio`, `Papel`) heredan de `Residuo` y pueden especializar esos metodos para representar materiales con procesos de clasificacion y reciclaje diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Residuo` sin perder el comportamiento particular de cada tipo.
