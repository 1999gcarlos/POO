# Caso 23 - Empresa de logistica

## Diagrama UML

```mermaid
classDiagram
    class Bodega {
        <<abstract>>
        +almacenar()
        +despachar()
    }

    class BodegaFria {
        +almacenar()
        +despachar()
    }

    class BodegaSeca {
        +almacenar()
        +despachar()
    }

    class BodegaAutomatizada {
        +almacenar()
        +despachar()
    }

    Bodega <|-- BodegaFria
    Bodega <|-- BodegaSeca
    Bodega <|-- BodegaAutomatizada
```

## Proceso

```mermaid
flowchart TD
    A["Crear una bodega"] --> B{"Seleccionar tipo"}
    B --> C["BodegaFria"]
    B --> D["BodegaSeca"]
    B --> E["BodegaAutomatizada"]
    C --> F["almacenar()"]
    D --> F
    E --> F
    F --> G["despachar()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Bodega` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `almacenar()` y `despachar()`.

Las clases hijas (`BodegaFria`, `BodegaSeca`, `BodegaAutomatizada`) heredan de `Bodega` y pueden especializar esos metodos para representar bodegas con condiciones de almacenamiento y despacho diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Bodega` sin perder el comportamiento particular de cada tipo.
