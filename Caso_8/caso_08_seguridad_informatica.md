# Caso 8 - Sistema de seguridad informatica

## Diagrama UML

```mermaid
classDiagram
    class SistemaSeguridad {
        <<abstract>>
        +escanear()
        +bloquear_amenaza()
    }

    class Antivirus
    class Firewall
    class IDS

    SistemaSeguridad <|-- Antivirus
    SistemaSeguridad <|-- Firewall
    SistemaSeguridad <|-- IDS
```

## Proceso

```mermaid
flowchart TD
    A["Iniciar proteccion"] --> B{"Mecanismo"}
    B --> C["Antivirus"]
    B --> D["Firewall"]
    B --> E["IDS"]
    C --> F["escanear()"]
    D --> F
    E --> F
    F --> G{"Amenaza detectada?"}
    G --> H["bloquear_amenaza()"]
    G --> I["Continuar monitoreo"]
```

## Explicacion

`SistemaSeguridad` define el comportamiento base. Cada mecanismo escanea y bloquea amenazas de forma especializada.
