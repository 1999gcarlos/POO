# Caso 27 - Sistema espacial

## Diagrama UML

```mermaid
classDiagram
    class MisionEspacial {
        <<abstract>>
        +despegar()
        +aterrizar()
    }

    class MisionLunar {
        +despegar()
        +aterrizar()
    }

    class MisionMarte {
        +despegar()
        +aterrizar()
    }

    class MisionSatelital {
        +despegar()
        +aterrizar()
    }

    MisionEspacial <|-- MisionLunar
    MisionEspacial <|-- MisionMarte
    MisionEspacial <|-- MisionSatelital
```

## Proceso

```mermaid
flowchart TD
    A["Crear una mision espacial"] --> B{"Seleccionar tipo"}
    B --> C["MisionLunar"]
    B --> D["MisionMarte"]
    B --> E["MisionSatelital"]
    C --> F["despegar()"]
    D --> F
    E --> F
    F --> G["aterrizar()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`MisionEspacial` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `despegar()` y `aterrizar()`.

Las clases hijas (`MisionLunar`, `MisionMarte`, `MisionSatelital`) heredan de `MisionEspacial` y pueden especializar esos metodos para representar misiones con objetivos, despegue y aterrizaje diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `MisionEspacial` sin perder el comportamiento particular de cada tipo.
