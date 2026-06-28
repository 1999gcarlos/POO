# Caso 14 - Sistema de correos

## Diagrama UML

```mermaid
classDiagram
    class Correspondencia {
        <<abstract>>
        +enviar()
        +rastrear()
    }

    class Carta {
        +enviar()
        +rastrear()
    }

    class Paquete {
        +enviar()
        +rastrear()
    }

    class DocumentoUrgente {
        +enviar()
        +rastrear()
    }

    Correspondencia <|-- Carta
    Correspondencia <|-- Paquete
    Correspondencia <|-- DocumentoUrgente
```

## Proceso

```mermaid
flowchart TD
    A["Crear una correspondencia"] --> B{"Seleccionar tipo"}
    B --> C["Carta"]
    B --> D["Paquete"]
    B --> E["DocumentoUrgente"]
    C --> F["enviar()"]
    D --> F
    E --> F
    F --> G["rastrear()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Correspondencia` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `enviar()` y `rastrear()`.

Las clases hijas (`Carta`, `Paquete`, `DocumentoUrgente`) heredan de `Correspondencia` y pueden especializar esos metodos para representar envios con seguimiento, prioridad y manejo diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Correspondencia` sin perder el comportamiento particular de cada tipo.
