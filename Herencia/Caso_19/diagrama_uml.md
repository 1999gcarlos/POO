# Caso 19 - Sistema de navegacion

## Diagrama UML

```mermaid
classDiagram
    class Navegador {
        <<abstract>>
        +calcular_ruta()
        +mostrar_mapa()
    }

    class GPSCarro {
        +calcular_ruta()
        +mostrar_mapa()
    }

    class GPSAvion {
        +calcular_ruta()
        +mostrar_mapa()
    }

    class GPSBarco {
        +calcular_ruta()
        +mostrar_mapa()
    }

    Navegador <|-- GPSCarro
    Navegador <|-- GPSAvion
    Navegador <|-- GPSBarco
```

## Proceso

```mermaid
flowchart TD
    A["Crear un navegador GPS"] --> B{"Seleccionar tipo"}
    B --> C["GPSCarro"]
    B --> D["GPSAvion"]
    B --> E["GPSBarco"]
    C --> F["calcular_ruta()"]
    D --> F
    E --> F
    F --> G["mostrar_mapa()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Navegador` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `calcular_ruta()` y `mostrar_mapa()`.

Las clases hijas (`GPSCarro`, `GPSAvion`, `GPSBarco`) heredan de `Navegador` y pueden especializar esos metodos para representar navegadores con rutas y mapas adaptados al medio de transporte. Esto aplica el principio de herencia y permite tratar todos los objetos como `Navegador` sin perder el comportamiento particular de cada tipo.
