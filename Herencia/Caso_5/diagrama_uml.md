# Caso 5 - Plataforma de mensajeria

## Diagrama UML

```mermaid
classDiagram
    class Mensaje {
        <<abstract>>
        +enviar()
        +eliminar()
    }

    class MensajeTexto {
        +enviar()
        +eliminar()
    }

    class MensajeVoz {
        +enviar()
        +eliminar()
    }

    class MensajeVideo {
        +enviar()
        +eliminar()
    }

    Mensaje <|-- MensajeTexto
    Mensaje <|-- MensajeVoz
    Mensaje <|-- MensajeVideo
```

## Proceso

```mermaid
flowchart TD
    A["Crear un mensaje"] --> B{"Seleccionar tipo"}
    B --> C["MensajeTexto"]
    B --> D["MensajeVoz"]
    B --> E["MensajeVideo"]
    C --> F["enviar()"]
    D --> F
    E --> F
    F --> G["eliminar()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Mensaje` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `enviar()` y `eliminar()`.

Las clases hijas (`MensajeTexto`, `MensajeVoz`, `MensajeVideo`) heredan de `Mensaje` y pueden especializar esos metodos para representar mensajes con formatos y comportamientos de envio diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Mensaje` sin perder el comportamiento particular de cada tipo.
