# Caso 20 - Plataforma de fotografia

## Diagrama UML

```mermaid
classDiagram
    class Camara {
        <<abstract>>
        +capturar()
        +guardar_imagen()
    }

    class CamaraProfesional {
        +capturar()
        +guardar_imagen()
    }

    class CamaraSeguridad {
        +capturar()
        +guardar_imagen()
    }

    class CamaraDrone {
        +capturar()
        +guardar_imagen()
    }

    Camara <|-- CamaraProfesional
    Camara <|-- CamaraSeguridad
    Camara <|-- CamaraDrone
```

## Proceso

```mermaid
flowchart TD
    A["Crear una camara"] --> B{"Seleccionar tipo"}
    B --> C["CamaraProfesional"]
    B --> D["CamaraSeguridad"]
    B --> E["CamaraDrone"]
    C --> F["capturar()"]
    D --> F
    E --> F
    F --> G["guardar_imagen()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Camara` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `capturar()` y `guardar_imagen()`.

Las clases hijas (`CamaraProfesional`, `CamaraSeguridad`, `CamaraDrone`) heredan de `Camara` y pueden especializar esos metodos para representar camaras con captura y almacenamiento adaptados al uso. Esto aplica el principio de herencia y permite tratar todos los objetos como `Camara` sin perder el comportamiento particular de cada tipo.
