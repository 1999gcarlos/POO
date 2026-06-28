# Caso 17 - Empresa de publicidad

## Diagrama UML

```mermaid
classDiagram
    class Campana {
        <<abstract>>
        +lanzar()
        +medir_resultados()
    }

    class CampanaTV {
        +lanzar()
        +medir_resultados()
    }

    class CampanaDigital {
        +lanzar()
        +medir_resultados()
    }

    class CampanaRadio {
        +lanzar()
        +medir_resultados()
    }

    Campana <|-- CampanaTV
    Campana <|-- CampanaDigital
    Campana <|-- CampanaRadio
```

## Proceso

```mermaid
flowchart TD
    A["Crear una campana publicitaria"] --> B{"Seleccionar tipo"}
    B --> C["CampanaTV"]
    B --> D["CampanaDigital"]
    B --> E["CampanaRadio"]
    C --> F["lanzar()"]
    D --> F
    E --> F
    F --> G["medir_resultados()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Campana` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `lanzar()` y `medir_resultados()`.

Las clases hijas (`CampanaTV`, `CampanaDigital`, `CampanaRadio`) heredan de `Campana` y pueden especializar esos metodos para representar campanas con medios, alcance y metricas diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Campana` sin perder el comportamiento particular de cada tipo.
