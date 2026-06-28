# Caso 21 - Sistema judicial

## Diagrama UML

```mermaid
classDiagram
    class ProcesoJudicial {
        <<abstract>>
        +iniciar_proceso()
        +cerrar_proceso()
    }

    class CasoCivil {
        +iniciar_proceso()
        +cerrar_proceso()
    }

    class CasoPenal {
        +iniciar_proceso()
        +cerrar_proceso()
    }

    class CasoLaboral {
        +iniciar_proceso()
        +cerrar_proceso()
    }

    ProcesoJudicial <|-- CasoCivil
    ProcesoJudicial <|-- CasoPenal
    ProcesoJudicial <|-- CasoLaboral
```

## Proceso

```mermaid
flowchart TD
    A["Crear un proceso judicial"] --> B{"Seleccionar tipo"}
    B --> C["CasoCivil"]
    B --> D["CasoPenal"]
    B --> E["CasoLaboral"]
    C --> F["iniciar_proceso()"]
    D --> F
    E --> F
    F --> G["cerrar_proceso()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`ProcesoJudicial` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `iniciar_proceso()` y `cerrar_proceso()`.

Las clases hijas (`CasoCivil`, `CasoPenal`, `CasoLaboral`) heredan de `ProcesoJudicial` y pueden especializar esos metodos para representar procesos legales con etapas y cierres diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `ProcesoJudicial` sin perder el comportamiento particular de cada tipo.
