# Caso 10 - Empresa agricola

## Diagrama UML

```mermaid
classDiagram
    class Cultivo {
        <<abstract>>
        +sembrar()
        +cosechar()
    }

    class CultivoMaiz {
        +sembrar()
        +cosechar()
    }

    class CultivoCafe {
        +sembrar()
        +cosechar()
    }

    class CultivoArroz {
        +sembrar()
        +cosechar()
    }

    Cultivo <|-- CultivoMaiz
    Cultivo <|-- CultivoCafe
    Cultivo <|-- CultivoArroz
```

## Proceso

```mermaid
flowchart TD
    A["Crear un cultivo"] --> B{"Seleccionar tipo"}
    B --> C["CultivoMaiz"]
    B --> D["CultivoCafe"]
    B --> E["CultivoArroz"]
    C --> F["sembrar()"]
    D --> F
    E --> F
    F --> G["cosechar()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Cultivo` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `sembrar()` y `cosechar()`.

Las clases hijas (`CultivoMaiz`, `CultivoCafe`, `CultivoArroz`) heredan de `Cultivo` y pueden especializar esos metodos para representar cultivos con ciclos de siembra y cosecha diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Cultivo` sin perder el comportamiento particular de cada tipo.
