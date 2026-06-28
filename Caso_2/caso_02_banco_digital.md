# Caso 2 - Banco digital

## Diagrama UML

```mermaid
classDiagram
    class CuentaBancaria {
        <<abstract>>
        +retirar()
        +depositar()
        +calcular_interes()
    }

    class CuentaAhorros
    class CuentaCorriente
    class CuentaEmpresarial

    CuentaBancaria <|-- CuentaAhorros
    CuentaBancaria <|-- CuentaCorriente
    CuentaBancaria <|-- CuentaEmpresarial
```

## Proceso

```mermaid
flowchart TD
    A["Crear cuenta bancaria"] --> B{"Tipo de cuenta"}
    B --> C["CuentaAhorros"]
    B --> D["CuentaCorriente"]
    B --> E["CuentaEmpresarial"]
    C --> F["depositar()"]
    D --> F
    E --> F
    F --> G["retirar()"]
    G --> H["calcular_interes()"]
    H --> I["Actualizar saldo"]
```

## Explicacion

`CuentaBancaria` define las operaciones comunes. Cada tipo de cuenta puede aplicar reglas diferentes para retiros, depositos e intereses.
