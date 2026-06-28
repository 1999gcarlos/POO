# Caso 24 - Sistema financiero

## Diagrama UML

```mermaid
classDiagram
    class Inversion {
        <<abstract>>
        +invertir()
        +calcular_ganancia()
    }

    class Acciones {
        +invertir()
        +calcular_ganancia()
    }

    class Criptomonedas {
        +invertir()
        +calcular_ganancia()
    }

    class Bonos {
        +invertir()
        +calcular_ganancia()
    }

    Inversion <|-- Acciones
    Inversion <|-- Criptomonedas
    Inversion <|-- Bonos
```

## Proceso

```mermaid
flowchart TD
    A["Crear una inversion"] --> B{"Seleccionar tipo"}
    B --> C["Acciones"]
    B --> D["Criptomonedas"]
    B --> E["Bonos"]
    C --> F["invertir()"]
    D --> F
    E --> F
    F --> G["calcular_ganancia()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Inversion` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `invertir()` y `calcular_ganancia()`.

Las clases hijas (`Acciones`, `Criptomonedas`, `Bonos`) heredan de `Inversion` y pueden especializar esos metodos para representar instrumentos financieros con riesgo y ganancia diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Inversion` sin perder el comportamiento particular de cada tipo.
