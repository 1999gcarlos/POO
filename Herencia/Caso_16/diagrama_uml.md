# Caso 16 - Sistema hotelero

## Diagrama UML

```mermaid
classDiagram
    class Habitacion {
        <<abstract>>
        +reservar()
        +liberar()
    }

    class HabitacionSimple {
        +reservar()
        +liberar()
    }

    class HabitacionDoble {
        +reservar()
        +liberar()
    }

    class Suite {
        +reservar()
        +liberar()
    }

    Habitacion <|-- HabitacionSimple
    Habitacion <|-- HabitacionDoble
    Habitacion <|-- Suite
```

## Proceso

```mermaid
flowchart TD
    A["Crear una habitacion"] --> B{"Seleccionar tipo"}
    B --> C["HabitacionSimple"]
    B --> D["HabitacionDoble"]
    B --> E["Suite"]
    C --> F["reservar()"]
    D --> F
    E --> F
    F --> G["liberar()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Habitacion` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `reservar()` y `liberar()`.

Las clases hijas (`HabitacionSimple`, `HabitacionDoble`, `Suite`) heredan de `Habitacion` y pueden especializar esos metodos para representar habitaciones con capacidad, tarifa y disponibilidad diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Habitacion` sin perder el comportamiento particular de cada tipo.
