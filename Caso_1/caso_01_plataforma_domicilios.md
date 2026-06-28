# Caso 1 - Plataforma de domicilios

## Diagrama UML

```mermaid
classDiagram
    class Entrega {
        <<abstract>>
        +calcular_tiempo()
        +asignar_repartidor()
    }

    class EntregaMoto
    class EntregaBicicleta
    class EntregaCarro

    Entrega <|-- EntregaMoto
    Entrega <|-- EntregaBicicleta
    Entrega <|-- EntregaCarro
```

## Proceso

```mermaid
flowchart TD
    A["Crear una entrega"] --> B{"Tipo de entrega"}
    B --> C["EntregaMoto"]
    B --> D["EntregaBicicleta"]
    B --> E["EntregaCarro"]
    C --> F["calcular_tiempo()"]
    D --> F
    E --> F
    F --> G["asignar_repartidor()"]
    G --> H["Mostrar informacion de la entrega"]
```

## Explicacion

`Entrega` es una clase abstracta. Las clases hijas representan medios de transporte diferentes y cada una puede calcular su tiempo y asignar su repartidor.
