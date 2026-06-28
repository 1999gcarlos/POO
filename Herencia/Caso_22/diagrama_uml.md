# Caso 22 - Plataforma de aprendizaje

## Diagrama UML

```mermaid
classDiagram
    class Evaluacion {
        <<abstract>>
        +calificar()
        +mostrar_resultado()
    }

    class Quiz {
        +calificar()
        +mostrar_resultado()
    }

    class ExamenFinal {
        +calificar()
        +mostrar_resultado()
    }

    class Taller {
        +calificar()
        +mostrar_resultado()
    }

    Evaluacion <|-- Quiz
    Evaluacion <|-- ExamenFinal
    Evaluacion <|-- Taller
```

## Proceso

```mermaid
flowchart TD
    A["Crear una evaluacion"] --> B{"Seleccionar tipo"}
    B --> C["Quiz"]
    B --> D["ExamenFinal"]
    B --> E["Taller"]
    C --> F["calificar()"]
    D --> F
    E --> F
    F --> G["mostrar_resultado()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Evaluacion` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `calificar()` y `mostrar_resultado()`.

Las clases hijas (`Quiz`, `ExamenFinal`, `Taller`) heredan de `Evaluacion` y pueden especializar esos metodos para representar evaluaciones con criterios y resultados diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Evaluacion` sin perder el comportamiento particular de cada tipo.
