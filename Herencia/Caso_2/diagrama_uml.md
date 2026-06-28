# Caso 2 - Plataforma de delivery de comida

## Diagrama UML

```mermaid
classDiagram
    class Restaurante {
        <<abstract>>
        +abrir_restaurante()
        +recibir_pedido()
    }

    class RestauranteRapido {
        +abrir_restaurante()
        +recibir_pedido()
    }

    class RestauranteGourmet {
        +abrir_restaurante()
        +recibir_pedido()
    }

    class RestauranteVegetariano {
        +abrir_restaurante()
        +recibir_pedido()
    }

    Restaurante <|-- RestauranteRapido
    Restaurante <|-- RestauranteGourmet
    Restaurante <|-- RestauranteVegetariano
```

## Proceso

```mermaid
flowchart TD
    A["Crear un restaurante asociado"] --> B{"Seleccionar tipo"}
    B --> C["RestauranteRapido"]
    B --> D["RestauranteGourmet"]
    B --> E["RestauranteVegetariano"]
    C --> F["abrir_restaurante()"]
    D --> F
    E --> F
    F --> G["recibir_pedido()"]
    G --> H["Mostrar resultado del proceso"]
```

## Explicacion

`Restaurante` es una clase abstracta que define el comportamiento comun del sistema mediante los metodos `abrir_restaurante()` y `recibir_pedido()`.

Las clases hijas (`RestauranteRapido`, `RestauranteGourmet`, `RestauranteVegetariano`) heredan de `Restaurante` y pueden especializar esos metodos para representar restaurantes con modelos de atencion y menus diferentes. Esto aplica el principio de herencia y permite tratar todos los objetos como `Restaurante` sin perder el comportamiento particular de cada tipo.
