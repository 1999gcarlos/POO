# Caso 15 - Plataforma de cursos deportivos

## Diagrama UML

```mermaid
classDiagram
    class Entrenamiento {
        <<abstract>>
        +iniciar()
        +finalizar()
    }

    class EntrenamientoFutbol {
        +iniciar()
        +finalizar()
    }

    class EntrenamientoNatacion {
        +iniciar()
        +finalizar()
    }

    class EntrenamientoBoxeo {
        +iniciar()
        +finalizar()
    }

    Entrenamiento <|-- EntrenamientoFutbol
    Entrenamiento <|-- EntrenamientoNatacion
    Entrenamiento <|-- EntrenamientoBoxeo
```

## Proceso

```mermaid
flowchart TD
    A["Crear un entrenamiento"] --> B{"Seleccionar tipo"}
    B --> C["EntrenamientoFutbol"]
    B --> D["EntrenamientoNatacion"]
    B --> E["EntrenamientoBoxeo"]
    C --> F["iniciar()"]
    D --> F
    E --> F
    F --> G["finalizar()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Entrenamiento` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `iniciar()` y `finalizar()`.

Las clases hijas (`EntrenamientoFutbol`, `EntrenamientoNatacion`, `EntrenamientoBoxeo`) heredan de `Entrenamiento` y pueden especializar esos metodos para representar disciplinas deportivas con rutinas y cierres diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Entrenamiento` sin perder el comportamiento particular de cada tipo.
