# Caso 13 - Empresa minera

## Diagrama UML

```mermaid
classDiagram
    class EquipoMinero {
        <<abstract>>
        +operar()
        +apagar()
    }

    class Perforadora {
        +operar()
        +apagar()
    }

    class ExcavadoraMineria {
        +operar()
        +apagar()
    }

    class Trituradora {
        +operar()
        +apagar()
    }

    EquipoMinero <|-- Perforadora
    EquipoMinero <|-- ExcavadoraMineria
    EquipoMinero <|-- Trituradora
```

## Proceso

```mermaid
flowchart TD
    A["Crear un equipo minero"] --> B{"Seleccionar tipo"}
    B --> C["Perforadora"]
    B --> D["ExcavadoraMineria"]
    B --> E["Trituradora"]
    C --> F["operar()"]
    D --> F
    E --> F
    F --> G["apagar()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`EquipoMinero` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `operar()` y `apagar()`.

Las clases hijas (`Perforadora`, `ExcavadoraMineria`, `Trituradora`) heredan de `EquipoMinero` y pueden especializar esos metodos para representar maquinas con operaciones y protocolos de apagado diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `EquipoMinero` sin perder el comportamiento particular de cada tipo.
