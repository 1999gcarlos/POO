# Caso 25 - Plataforma de redes sociales

## Diagrama UML

```mermaid
classDiagram
    class ContenidoSocial {
        <<abstract>>
        +publicar()
        +eliminar()
    }

    class Foto {
        +publicar()
        +eliminar()
    }

    class Video {
        +publicar()
        +eliminar()
    }

    class Historia {
        +publicar()
        +eliminar()
    }

    ContenidoSocial <|-- Foto
    ContenidoSocial <|-- Video
    ContenidoSocial <|-- Historia
```

## Proceso

```mermaid
flowchart TD
    A["Crear un contenido social"] --> B{"Seleccionar tipo"}
    B --> C["Foto"]
    B --> D["Video"]
    B --> E["Historia"]
    C --> F["publicar()"]
    D --> F
    E --> F
    F --> G["eliminar()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`ContenidoSocial` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `publicar()` y `eliminar()`.

Las clases hijas (`Foto`, `Video`, `Historia`) heredan de `ContenidoSocial` y pueden especializar esos metodos para representar publicaciones con formatos y permanencia diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `ContenidoSocial` sin perder el comportamiento particular de cada tipo.
