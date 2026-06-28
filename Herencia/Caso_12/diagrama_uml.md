# Caso 12 - Plataforma de mascotas

## Diagrama UML

```mermaid
classDiagram
    class Mascota {
        <<abstract>>
        +vacunar()
        +alimentar()
    }

    class Perro {
        +vacunar()
        +alimentar()
    }

    class Gato {
        +vacunar()
        +alimentar()
    }

    class Conejo {
        +vacunar()
        +alimentar()
    }

    Mascota <|-- Perro
    Mascota <|-- Gato
    Mascota <|-- Conejo
```

## Proceso

```mermaid
flowchart TD
    A["Crear una mascota"] --> B{"Seleccionar tipo"}
    B --> C["Perro"]
    B --> D["Gato"]
    B --> E["Conejo"]
    C --> F["vacunar()"]
    D --> F
    E --> F
    F --> G["alimentar()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Mascota` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `vacunar()` y `alimentar()`.

Las clases hijas (`Perro`, `Gato`, `Conejo`) heredan de `Mascota` y pueden especializar esos metodos para representar animales con cuidados, vacunas y alimentacion diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Mascota` sin perder el comportamiento particular de cada tipo.
