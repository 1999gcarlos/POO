# Caso 1 - Sistema de gimnasio

## Diagrama UML

```mermaid
classDiagram
    class Miembro {
        <<abstract>>
        +ingresar_gimnasio()
        +pagar_mensualidad()
    }

    class MiembroBasico {
        +ingresar_gimnasio()
        +pagar_mensualidad()
    }

    class MiembroPremium {
        +ingresar_gimnasio()
        +pagar_mensualidad()
    }

    class MiembroVIP {
        +ingresar_gimnasio()
        +pagar_mensualidad()
    }

    Miembro <|-- MiembroBasico
    Miembro <|-- MiembroPremium
    Miembro <|-- MiembroVIP
```

## Proceso

```mermaid
flowchart TD
    A["Crear un miembro del gimnasio"] --> B{"Seleccionar tipo"}
    B --> C["MiembroBasico"]
    B --> D["MiembroPremium"]
    B --> E["MiembroVIP"]
    C --> F["ingresar_gimnasio()"]
    D --> F
    E --> F
    F --> G["pagar_mensualidad()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Miembro` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `ingresar_gimnasio()` y `pagar_mensualidad()`.

Las clases hijas (`MiembroBasico`, `MiembroPremium`, `MiembroVIP`) heredan de `Miembro` y pueden especializar esos metodos para representar tipos de membresia con beneficios y reglas de pago diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Miembro` sin perder el comportamiento particular de cada tipo.
