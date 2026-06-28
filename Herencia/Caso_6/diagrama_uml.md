# Caso 6 - Sistema de supermercado

## Diagrama UML

```mermaid
classDiagram
    class Producto {
        <<abstract>>
        +calcular_precio()
        +verificar_stock()
    }

    class Lacteo {
        +calcular_precio()
        +verificar_stock()
    }

    class Bebida {
        +calcular_precio()
        +verificar_stock()
    }

    class Enlatado {
        +calcular_precio()
        +verificar_stock()
    }

    Producto <|-- Lacteo
    Producto <|-- Bebida
    Producto <|-- Enlatado
```

## Proceso

```mermaid
flowchart TD
    A["Crear un producto alimenticio"] --> B{"Seleccionar tipo"}
    B --> C["Lacteo"]
    B --> D["Bebida"]
    B --> E["Enlatado"]
    C --> F["calcular_precio()"]
    D --> F
    E --> F
    F --> G["verificar_stock()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Producto` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `calcular_precio()` y `verificar_stock()`.

Las clases hijas (`Lacteo`, `Bebida`, `Enlatado`) heredan de `Producto` y pueden especializar esos metodos para representar productos con reglas de precio, existencia y manejo diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Producto` sin perder el comportamiento particular de cada tipo.
