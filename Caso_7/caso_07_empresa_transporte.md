# Caso 7 - Empresa de transporte

## Diagrama UML

```mermaid
classDiagram
    class Vehiculo {
        <<abstract>>
        +arrancar()
        +detener()
        +calcular_combustible()
    }

    class Bus
    class Taxi
    class Camion

    Vehiculo <|-- Bus
    Vehiculo <|-- Taxi
    Vehiculo <|-- Camion
```

## Proceso

```mermaid
flowchart TD
    A["Registrar vehiculo"] --> B{"Tipo de vehiculo"}
    B --> C["Bus"]
    B --> D["Taxi"]
    B --> E["Camion"]
    C --> F["arrancar()"]
    D --> F
    E --> F
    F --> G["calcular_combustible()"]
    G --> H["detener()"]
```

## Explicacion

`Vehiculo` agrupa las operaciones comunes. Cada vehiculo calcula combustible de acuerdo con su uso y caracteristicas.
