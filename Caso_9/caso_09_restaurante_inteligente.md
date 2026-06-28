# Caso 9 - Restaurante inteligente

## Diagrama UML

```mermaid
classDiagram
    class Pedido {
        <<abstract>>
        +calcular_total()
        +generar_factura()
    }

    class PedidoMesa
    class PedidoDomicilio
    class PedidoExpress

    Pedido <|-- PedidoMesa
    Pedido <|-- PedidoDomicilio
    Pedido <|-- PedidoExpress
```

## Proceso

```mermaid
flowchart TD
    A["Crear pedido"] --> B{"Tipo de pedido"}
    B --> C["PedidoMesa"]
    B --> D["PedidoDomicilio"]
    B --> E["PedidoExpress"]
    C --> F["calcular_total()"]
    D --> F
    E --> F
    F --> G["generar_factura()"]
    G --> H["Entregar factura al cliente"]
```

## Explicacion

`Pedido` define las operaciones comunes. Cada tipo puede calcular total con reglas propias, como domicilio o prioridad express.
