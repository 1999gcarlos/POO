# Caso 25 - Aeropuerto internacional

## Diagrama UML

```mermaid
classDiagram
    class Vuelo {
        <<abstract>>
        +despegar()
        +aterrizar()
    }

    class VueloNacional
    class VueloInternacional
    class VueloCarga

    Vuelo <|-- VueloNacional
    Vuelo <|-- VueloInternacional
    Vuelo <|-- VueloCarga
```

## Proceso

```mermaid
flowchart TD
    A["Programar vuelo"] --> B{"Tipo de vuelo"}
    B --> C["VueloNacional"]
    B --> D["VueloInternacional"]
    B --> E["VueloCarga"]
    C --> F["despegar()"]
    D --> F
    E --> F
    F --> G["Completar ruta"]
    G --> H["aterrizar()"]
```

## Explicacion

`Vuelo` define las operaciones principales. Cada tipo de vuelo despega y aterriza siguiendo reglas distintas del aeropuerto.
