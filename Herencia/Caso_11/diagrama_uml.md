# Caso 11 - Sistema de cine

## Diagrama UML

```mermaid
classDiagram
    class Funcion {
        <<abstract>>
        +iniciar_funcion()
        +vender_boletos()
    }

    class Funcion2D {
        +iniciar_funcion()
        +vender_boletos()
    }

    class Funcion3D {
        +iniciar_funcion()
        +vender_boletos()
    }

    class FuncionVIP {
        +iniciar_funcion()
        +vender_boletos()
    }

    Funcion <|-- Funcion2D
    Funcion <|-- Funcion3D
    Funcion <|-- FuncionVIP
```

## Proceso

```mermaid
flowchart TD
    A["Crear una funcion de cine"] --> B{"Seleccionar tipo"}
    B --> C["Funcion2D"]
    B --> D["Funcion3D"]
    B --> E["FuncionVIP"]
    C --> F["iniciar_funcion()"]
    D --> F
    E --> F
    F --> G["vender_boletos()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Funcion` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `iniciar_funcion()` y `vender_boletos()`.

Las clases hijas (`Funcion2D`, `Funcion3D`, `FuncionVIP`) heredan de `Funcion` y pueden especializar esos metodos para representar funciones con experiencia, precio y salas diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Funcion` sin perder el comportamiento particular de cada tipo.
