# Caso 9 - Plataforma de noticias

## Diagrama UML

```mermaid
classDiagram
    class Publicacion {
        <<abstract>>
        +publicar()
        +editar()
    }

    class Noticia {
        +publicar()
        +editar()
    }

    class Articulo {
        +publicar()
        +editar()
    }

    class Entrevista {
        +publicar()
        +editar()
    }

    Publicacion <|-- Noticia
    Publicacion <|-- Articulo
    Publicacion <|-- Entrevista
```

## Proceso

```mermaid
flowchart TD
    A["Crear una publicacion"] --> B{"Seleccionar tipo"}
    B --> C["Noticia"]
    B --> D["Articulo"]
    B --> E["Entrevista"]
    C --> F["publicar()"]
    D --> F
    E --> F
    F --> G["editar()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Publicacion` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `publicar()` y `editar()`.

Las clases hijas (`Noticia`, `Articulo`, `Entrevista`) heredan de `Publicacion` y pueden especializar esos metodos para representar contenidos editoriales con estructura y revision diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Publicacion` sin perder el comportamiento particular de cada tipo.
