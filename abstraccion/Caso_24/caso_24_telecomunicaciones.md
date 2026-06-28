# Caso 24 - Empresa de telecomunicaciones

## Diagrama UML

```mermaid
classDiagram
    class ServicioTelecomunicacion {
        <<abstract>>
        +activar_servicio()
        +calcular_tarifa()
    }

    class Internet
    class Telefonia
    class Television

    ServicioTelecomunicacion <|-- Internet
    ServicioTelecomunicacion <|-- Telefonia
    ServicioTelecomunicacion <|-- Television
```

## Proceso

```mermaid
flowchart TD
    A["Cliente solicita servicio"] --> B{"Servicio"}
    B --> C["Internet"]
    B --> D["Telefonia"]
    B --> E["Television"]
    C --> F["activar_servicio()"]
    D --> F
    E --> F
    F --> G["calcular_tarifa()"]
    G --> H["Mostrar valor mensual"]
```

## Explicacion

`ServicioTelecomunicacion` define activacion y tarifa. Cada servicio calcula el cobro de acuerdo con sus caracteristicas.
