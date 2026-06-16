# Diagrama UML y procesos - Banco Digital

Este documento explica la estructura del programa de banco digital y los procesos principales de la interfaz grafica.

## 1. Diagrama UML de clases

```mermaid
classDiagram
    class ABC

    class Cuenta {
        <<abstract>>
        +str numero
        +Cliente titular
        +float saldo
        +list~str~ movimientos
        +__init__(numero, titular, saldo)
        +obtener_tipo()* str
        +depositar(monto) bool
        +retirar(monto) bool
        +transferir(cuenta_destino, monto) bool
        +mostrar_info() void
        +mostrar_movimientos() void
    }

    class CuentaAhorros {
        +obtener_tipo() str
        +aplicar_interes(porcentaje) bool
    }

    class CuentaCorriente {
        +obtener_tipo() str
    }

    class Cliente {
        +str nombre
        +str documento
        +list~Cuenta~ cuentas
        +__init__(nombre, documento)
        +agregar_cuenta(cuenta) void
        +mostrar_cuentas() void
        +__str__() str
    }

    class BancoDigital {
        +str nombre
        +list~Cliente~ clientes
        +list~Cuenta~ cuentas
        +__init__(nombre)
        +registrar_cliente(cliente) void
        +abrir_cuenta(cliente, cuenta) void
        +buscar_cuenta(numero) Cuenta
        +mostrar_resumen() void
    }

    class InterfazBancoDigital {
        +Tk ventana
        +BancoDigital banco
        +StringVar tipo_cuenta
        +crear_componentes() void
        +registrar_cliente() void
        +abrir_cuenta() void
        +depositar() void
        +retirar() void
        +transferir() void
        +aplicar_interes() void
        +ver_movimientos() void
        +ver_resumen() void
    }

    ABC <|-- Cuenta
    Cuenta <|-- CuentaAhorros
    Cuenta <|-- CuentaCorriente
    Cliente o-- Cuenta : posee
    BancoDigital o-- Cliente : registra
    BancoDigital o-- Cuenta : administra
    InterfazBancoDigital --> BancoDigital : usa
    InterfazBancoDigital --> Cliente : crea
    InterfazBancoDigital --> CuentaAhorros : crea
    InterfazBancoDigital --> CuentaCorriente : crea
```

### Explicacion del UML

- `Cuenta` es una clase abstracta: define la estructura comun de todas las cuentas.
- `CuentaAhorros` y `CuentaCorriente` heredan de `Cuenta`.
- `Cliente` contiene una lista de cuentas.
- `BancoDigital` administra clientes y cuentas.
- `InterfazBancoDigital` conecta la ventana grafica con las clases del banco.

## 2. Proceso general del programa

```mermaid
flowchart TD
    A["Ejecutar interfaz_banco_digital.py"] --> B["Crear ventana Tkinter"]
    B --> C["Crear objeto InterfazBancoDigital"]
    C --> D["Crear objeto BancoDigital"]
    D --> E["Mostrar paneles de cliente, cuenta y operaciones"]
    E --> F["Usuario interactua con la interfaz"]
```

### Explicacion

La interfaz crea una instancia de `BancoDigital`. Ese objeto guarda los clientes y las cuentas creadas durante el uso del programa.

## 3. Proceso para registrar cliente

```mermaid
flowchart TD
    A["Usuario escribe nombre"] --> B["Usuario escribe documento"]
    B --> C["Presiona Agregar cliente"]
    C --> D{"Nombre y documento completos?"}
    D -- "No" --> E["Mostrar advertencia"]
    D -- "Si" --> F["Crear objeto Cliente"]
    F --> G["Registrar cliente en BancoDigital"]
    G --> H["Mostrar cliente en lista visual"]
    H --> I["Mostrar mensaje de confirmacion"]
    I --> J["Limpiar campos"]
```

### Explicacion

La interfaz valida los campos y luego crea un objeto `Cliente`. Ese cliente se guarda en la lista `banco.clientes`.

## 4. Proceso para abrir cuenta

```mermaid
flowchart TD
    A["Usuario selecciona cliente"] --> B["Escribe numero de cuenta"]
    B --> C["Escribe saldo inicial"]
    C --> D["Selecciona tipo: Ahorros o Corriente"]
    D --> E["Presiona Abrir cuenta"]
    E --> F{"Cliente seleccionado?"}
    F -- "No" --> G["Mostrar advertencia"]
    F -- "Si" --> H{"Numero de cuenta valido?"}
    H -- "No" --> I["Mostrar advertencia"]
    H -- "Si" --> J{"La cuenta ya existe?"}
    J -- "Si" --> K["Mostrar advertencia de cuenta repetida"]
    J -- "No" --> L{"Saldo numerico y no negativo?"}
    L -- "No" --> M["Mostrar advertencia"]
    L -- "Si" --> N{"Tipo de cuenta"}
    N -- "Ahorros" --> O["Crear CuentaAhorros"]
    N -- "Corriente" --> P["Crear CuentaCorriente"]
    O --> Q["BancoDigital.abrir_cuenta(cliente, cuenta)"]
    P --> Q
    Q --> R["Agregar cuenta a banco.cuentas"]
    R --> S["Agregar cuenta a cliente.cuentas"]
    S --> T["Mostrar cuenta en lista visual"]
```

### Explicacion

Este proceso demuestra herencia y polimorfismo. La interfaz crea una cuenta de ahorros o corriente, pero ambas se manejan como objetos de tipo `Cuenta`.

## 5. Proceso para depositar

```mermaid
flowchart TD
    A["Usuario selecciona cuenta"] --> B["Escribe monto"]
    B --> C["Presiona Depositar"]
    C --> D{"Cuenta seleccionada?"}
    D -- "No" --> E["Mostrar advertencia"]
    D -- "Si" --> F{"Monto numerico?"}
    F -- "No" --> G["Mostrar advertencia"]
    F -- "Si" --> H["Llamar cuenta.depositar(monto)"]
    H --> I{"Monto mayor que cero?"}
    I -- "No" --> J["Mostrar error"]
    I -- "Si" --> K["Aumentar saldo"]
    K --> L["Registrar movimiento"]
    L --> M["Actualizar lista de cuentas"]
```

### Explicacion

El metodo `depositar()` pertenece a la clase `Cuenta`, por eso funciona tanto para cuentas de ahorros como para cuentas corrientes.

## 6. Proceso para retirar

```mermaid
flowchart TD
    A["Usuario selecciona cuenta"] --> B["Escribe monto"]
    B --> C["Presiona Retirar"]
    C --> D{"Cuenta seleccionada?"}
    D -- "No" --> E["Mostrar advertencia"]
    D -- "Si" --> F{"Monto numerico?"}
    F -- "No" --> G["Mostrar advertencia"]
    F -- "Si" --> H["Llamar cuenta.retirar(monto)"]
    H --> I{"Monto mayor que cero?"}
    I -- "No" --> J["Mostrar error"]
    I -- "Si" --> K{"Saldo suficiente?"}
    K -- "No" --> L["Mostrar fondos insuficientes"]
    K -- "Si" --> M["Disminuir saldo"]
    M --> N["Registrar movimiento"]
    N --> O["Actualizar lista de cuentas"]
```

### Explicacion

El retiro valida que el monto sea positivo y que la cuenta tenga saldo suficiente antes de modificar el saldo.

## 7. Proceso para transferir

```mermaid
flowchart TD
    A["Usuario selecciona cuenta origen"] --> B["Escribe monto"]
    B --> C["Escribe numero de cuenta destino"]
    C --> D["Presiona Transferir"]
    D --> E{"Cuenta origen seleccionada?"}
    E -- "No" --> F["Mostrar advertencia"]
    E -- "Si" --> G{"Monto numerico?"}
    G -- "No" --> H["Mostrar advertencia"]
    G -- "Si" --> I{"Cuenta destino existe?"}
    I -- "No" --> J["Mostrar advertencia"]
    I -- "Si" --> K["Llamar cuenta_origen.transferir(cuenta_destino, monto)"]
    K --> L["Retirar dinero de cuenta origen"]
    L --> M{"Retiro exitoso?"}
    M -- "No" --> N["Cancelar transferencia"]
    M -- "Si" --> O["Depositar dinero en cuenta destino"]
    O --> P["Registrar movimientos en ambas cuentas"]
    P --> Q["Actualizar lista de cuentas"]
```

### Explicacion

La transferencia reutiliza dos metodos ya existentes: `retirar()` y `depositar()`. Asi se evita duplicar logica.

## 8. Proceso para aplicar interes

```mermaid
flowchart TD
    A["Usuario selecciona cuenta"] --> B["Escribe porcentaje"]
    B --> C["Presiona Aplicar interes"]
    C --> D{"Cuenta seleccionada?"}
    D -- "No" --> E["Mostrar advertencia"]
    D -- "Si" --> F{"Porcentaje numerico?"}
    F -- "No" --> G["Mostrar advertencia"]
    F -- "Si" --> H{"La cuenta es CuentaAhorros?"}
    H -- "No" --> I["Mostrar: operacion no disponible"]
    H -- "Si" --> J["Llamar cuenta.aplicar_interes(porcentaje)"]
    J --> K{"Porcentaje mayor que cero?"}
    K -- "No" --> L["Mostrar error"]
    K -- "Si" --> M["Calcular interes"]
    M --> N["Aumentar saldo"]
    N --> O["Registrar movimiento"]
    O --> P["Actualizar lista de cuentas"]
```

### Explicacion

El interes solo existe en `CuentaAhorros`. La interfaz verifica el tipo del objeto antes de llamar ese metodo.

## 9. Proceso para ver movimientos

```mermaid
flowchart TD
    A["Usuario selecciona cuenta"] --> B["Presiona Ver movimientos"]
    B --> C{"Cuenta seleccionada?"}
    C -- "No" --> D["Mostrar advertencia"]
    C -- "Si" --> E["Llamar cuenta.mostrar_movimientos()"]
    E --> F{"Hay movimientos?"}
    F -- "No" --> G["Mostrar que no hay movimientos"]
    F -- "Si" --> H["Mostrar cada movimiento"]
```

### Explicacion

Cada cuenta guarda su propio historial en el atributo `movimientos`. Eso es encapsulamiento: la informacion pertenece al objeto cuenta.

## 10. Proceso para ver resumen

```mermaid
flowchart TD
    A["Usuario presiona Ver resumen"] --> B["Limpiar mensajes anteriores"]
    B --> C["Llamar banco.mostrar_resumen()"]
    C --> D["Mostrar clientes registrados"]
    D --> E["Mostrar cuentas registradas"]
    E --> F["Mostrar titular, tipo y saldo de cada cuenta"]
```

### Explicacion

El resumen consulta el estado actual del objeto `BancoDigital`, mostrando las listas de clientes y cuentas registradas.

## 11. Conceptos POO usados

| Concepto | Donde aparece | Explicacion |
| --- | --- | --- |
| Clase | `Cliente`, `Cuenta`, `BancoDigital` | Molde para crear objetos. |
| Objeto | `Cliente(nombre, documento)` | Instancia creada desde una clase. |
| Atributo | `saldo`, `numero`, `clientes`, `cuentas` | Dato guardado dentro del objeto. |
| Metodo | `depositar()`, `retirar()`, `transferir()` | Accion que pertenece a una clase. |
| Abstraccion | `Cuenta(ABC)` | Plantilla general para cuentas bancarias. |
| Herencia | `CuentaAhorros(Cuenta)` | Una clase hija reutiliza codigo de la clase padre. |
| Polimorfismo | `obtener_tipo()` | El mismo metodo devuelve resultados diferentes segun la clase. |
| Encapsulamiento | `self.saldo`, `self.movimientos` | Los datos se guardan dentro del objeto que los maneja. |
| Composicion | `Cliente` contiene cuentas | Un objeto administra una lista de otros objetos. |
