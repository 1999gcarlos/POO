# Caso 3 - Sistema de biblioteca

## Diagrama UML

```mermaid
classDiagram
    class MaterialBiblioteca {
        <<abstract>>
        +prestar()
        +devolver()
    }

    class Libro {
        +prestar()
        +devolver()
    }

    class Revista {
        +prestar()
        +devolver()
    }

    class Tesis {
        +prestar()
        +devolver()
    }

    MaterialBiblioteca <|-- Libro
    MaterialBiblioteca <|-- Revista
    MaterialBiblioteca <|-- Tesis
```

## Proceso

```mermaid
flowchart TD
    A["Crear un material de biblioteca"] --> B{"Seleccionar tipo"}
    B --> C["Libro"]
    B --> D["Revista"]
    B --> E["Tesis"]
    C --> F["prestar()"]
    D --> F
    E --> F
    F --> G["devolver()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`MaterialBiblioteca` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `prestar()` y `devolver()`.

Las clases hijas (`Libro`, `Revista`, `Tesis`) heredan de `MaterialBiblioteca` y pueden especializar esos metodos para representar materiales con condiciones de prestamo y devolucion diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `MaterialBiblioteca` sin perder el comportamiento particular de cada tipo.
