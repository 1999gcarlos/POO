# Caso 8 - Sistema de impresion

## Diagrama UML

```mermaid
classDiagram
    class Impresora {
        <<abstract>>
        +imprimir()
        +cancelar_impresion()
    }

    class ImpresoraLaser {
        +imprimir()
        +cancelar_impresion()
    }

    class Impresora3D {
        +imprimir()
        +cancelar_impresion()
    }

    class ImpresoraTinta {
        +imprimir()
        +cancelar_impresion()
    }

    Impresora <|-- ImpresoraLaser
    Impresora <|-- Impresora3D
    Impresora <|-- ImpresoraTinta
```

## Proceso

```mermaid
flowchart TD
    A["Crear una impresora"] --> B{"Seleccionar tipo"}
    B --> C["ImpresoraLaser"]
    B --> D["Impresora3D"]
    B --> E["ImpresoraTinta"]
    C --> F["imprimir()"]
    D --> F
    E --> F
    F --> G["cancelar_impresion()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Impresora` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `imprimir()` y `cancelar_impresion()`.

Las clases hijas (`ImpresoraLaser`, `Impresora3D`, `ImpresoraTinta`) heredan de `Impresora` y pueden especializar esos metodos para representar impresoras con tecnologias y procesos de impresion diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Impresora` sin perder el comportamiento particular de cada tipo.
