# Caso 16 - Plataforma de musica

## Diagrama UML

```mermaid
classDiagram
    class Audio {
        <<abstract>>
        +reproducir()
        +detener()
    }

    class Cancion
    class Podcast
    class Audiolibro

    Audio <|-- Cancion
    Audio <|-- Podcast
    Audio <|-- Audiolibro
```

## Proceso

```mermaid
flowchart TD
    A["Seleccionar audio"] --> B{"Tipo de audio"}
    B --> C["Cancion"]
    B --> D["Podcast"]
    B --> E["Audiolibro"]
    C --> F["reproducir()"]
    D --> F
    E --> F
    F --> G["detener()"]
    G --> H["Guardar posicion de reproduccion"]
```

## Explicacion

`Audio` define el comportamiento comun. Canciones, podcasts y audiolibros se reproducen y detienen con el mismo contrato.
