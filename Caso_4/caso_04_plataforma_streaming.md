# Caso 4 - Plataforma de streaming

## Diagrama UML

```mermaid
classDiagram
    class Contenido {
        <<abstract>>
        +reproducir()
        +pausar()
    }

    class Pelicula
    class Serie
    class Documental

    Contenido <|-- Pelicula
    Contenido <|-- Serie
    Contenido <|-- Documental
```

## Proceso

```mermaid
flowchart TD
    A["Seleccionar contenido"] --> B{"Tipo de contenido"}
    B --> C["Pelicula"]
    B --> D["Serie"]
    B --> E["Documental"]
    C --> F["reproducir()"]
    D --> F
    E --> F
    F --> G["pausar()"]
    G --> H["Guardar estado de reproduccion"]
```

## Explicacion

`Contenido` representa cualquier multimedia. Las clases hijas permiten reproducir y pausar elementos distintos de la plataforma.
