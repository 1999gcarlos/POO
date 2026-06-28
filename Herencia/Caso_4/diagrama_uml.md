# Caso 4 - Empresa de energia

## Diagrama UML

```mermaid
classDiagram
    class FuenteEnergia {
        <<abstract>>
        +generar_energia()
        +medir_consumo()
    }

    class EnergiaSolar {
        +generar_energia()
        +medir_consumo()
    }

    class EnergiaEolica {
        +generar_energia()
        +medir_consumo()
    }

    class EnergiaHidraulica {
        +generar_energia()
        +medir_consumo()
    }

    FuenteEnergia <|-- EnergiaSolar
    FuenteEnergia <|-- EnergiaEolica
    FuenteEnergia <|-- EnergiaHidraulica
```

## Proceso

```mermaid
flowchart TD
    A["Crear una fuente de energia"] --> B{"Seleccionar tipo"}
    B --> C["EnergiaSolar"]
    B --> D["EnergiaEolica"]
    B --> E["EnergiaHidraulica"]
    C --> F["generar_energia()"]
    D --> F
    E --> F
    F --> G["medir_consumo()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`FuenteEnergia` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `generar_energia()` y `medir_consumo()`.

Las clases hijas (`EnergiaSolar`, `EnergiaEolica`, `EnergiaHidraulica`) heredan de `FuenteEnergia` y pueden especializar esos metodos para representar fuentes energeticas con formas distintas de generacion y medicion. Esto aplica el principio de herencia y permite tratar todos los objetos como `FuenteEnergia` sin perder el comportamiento particular de cada tipo.
