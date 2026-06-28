# Caso 7 - Empresa de eventos

## Diagrama UML

```mermaid
classDiagram
    class Evento {
        <<abstract>>
        +iniciar_evento()
        +finalizar_evento()
    }

    class Concierto {
        +iniciar_evento()
        +finalizar_evento()
    }

    class Conferencia {
        +iniciar_evento()
        +finalizar_evento()
    }

    class FiestaPrivada {
        +iniciar_evento()
        +finalizar_evento()
    }

    Evento <|-- Concierto
    Evento <|-- Conferencia
    Evento <|-- FiestaPrivada
```

## Proceso

```mermaid
flowchart TD
    A["Crear un evento"] --> B{"Seleccionar tipo"}
    B --> C["Concierto"]
    B --> D["Conferencia"]
    B --> E["FiestaPrivada"]
    C --> F["iniciar_evento()"]
    D --> F
    E --> F
    F --> G["finalizar_evento()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Evento` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `iniciar_evento()` y `finalizar_evento()`.

Las clases hijas (`Concierto`, `Conferencia`, `FiestaPrivada`) heredan de `Evento` y pueden especializar esos metodos para representar eventos con organizacion, duracion y cierre diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Evento` sin perder el comportamiento particular de cada tipo.
