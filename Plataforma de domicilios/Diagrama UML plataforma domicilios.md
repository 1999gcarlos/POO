# Diagrama UML y procesos - Plataforma de Domicilios

Este documento explica la estructura del programa de domicilios y los procesos principales de la interfaz grafica.

## 1. Diagrama UML de clases

```mermaid
classDiagram
    class ABC

    class Entrega {
        <<abstract>>
        +str destino
        +float distancia
        +__init__(destino, distancia)
        +calcular_tiempo()* int
        +asignar_repartidor()* str
        +mostrar_resumen() void
    }

    class EntregaMoto {
        +int VELOCIDAD_PROMEDIO
        +calcular_tiempo() int
        +asignar_repartidor() str
    }

    class EntregaBicicleta {
        +int VELOCIDAD_PROMEDIO
        +calcular_tiempo() int
        +asignar_repartidor() str
    }

    class EntregaCarro {
        +int VELOCIDAD_PROMEDIO
        +calcular_tiempo() int
        +asignar_repartidor() str
    }

    class PlataformaDomicilios {
        +str nombre
        +list~Entrega~ entregas
        +__init__(nombre)
        +registrar_entrega(entrega) void
        +mostrar_entregas() void
    }

    class InterfazDomicilios {
        +Tk ventana
        +PlataformaDomicilios plataforma
        +StringVar tipo_entrega
        +crear_componentes() void
        +registrar_entrega() void
        +crear_entrega(destino, distancia) Entrega
        +agregar_entrega_a_tabla(entrega) void
        +ver_entregas() void
        +limpiar_campos() void
        +limpiar_salida() void
        +mostrar_mensaje(mensaje) void
    }

    ABC <|-- Entrega
    Entrega <|-- EntregaMoto
    Entrega <|-- EntregaBicicleta
    Entrega <|-- EntregaCarro
    PlataformaDomicilios o-- Entrega : registra
    InterfazDomicilios --> PlataformaDomicilios : administra
    InterfazDomicilios --> EntregaMoto : crea
    InterfazDomicilios --> EntregaBicicleta : crea
    InterfazDomicilios --> EntregaCarro : crea
```

### Explicacion del UML

- `Entrega` es una clase abstracta: define lo que toda entrega debe tener.
- `EntregaMoto`, `EntregaBicicleta` y `EntregaCarro` heredan de `Entrega`.
- Cada tipo de entrega implementa `calcular_tiempo()` y `asignar_repartidor()`.
- `PlataformaDomicilios` guarda una lista de entregas.
- `InterfazDomicilios` usa la plataforma y crea objetos segun lo que seleccione el usuario.

## 2. Proceso general del programa

```mermaid
flowchart TD
    A["Ejecutar interfaz_domicilios.py"] --> B["Crear ventana Tkinter"]
    B --> C["Crear objeto InterfazDomicilios"]
    C --> D["Crear objeto PlataformaDomicilios"]
    D --> E["Mostrar campos, botones, tabla y mensajes"]
    E --> F["Usuario interactua con la interfaz"]
```

### Explicacion

El archivo `interfaz_domicilios.py` inicia la ventana. Dentro de esa ventana se crea una instancia de `PlataformaDomicilios`, que sera la encargada de guardar todas las entregas.

## 3. Proceso para registrar una entrega

```mermaid
flowchart TD
    A["Usuario escribe destino"] --> B["Usuario escribe distancia"]
    B --> C["Usuario selecciona tipo: Moto, Bicicleta o Carro"]
    C --> D["Presiona Registrar entrega"]
    D --> E{"Destino esta completo?"}
    E -- "No" --> F["Mostrar advertencia: escribe el destino"]
    E -- "Si" --> G{"Distancia es numerica?"}
    G -- "No" --> H["Mostrar advertencia: distancia invalida"]
    G -- "Si" --> I["Convertir distancia a float"]
    I --> J{"Distancia mayor que cero?"}
    J -- "No" --> K["Mostrar advertencia: distancia debe ser mayor que cero"]
    J -- "Si" --> L["Crear entrega segun tipo seleccionado"]
    L --> M["Registrar entrega en PlataformaDomicilios"]
    M --> N["Agregar entrega a la tabla"]
    N --> O["Mostrar mensaje de confirmacion"]
    O --> P["Limpiar campos"]
```

### Explicacion

La interfaz valida los datos antes de crear el objeto. Si todo es correcto, crea una entrega concreta y la guarda en la plataforma.

## 4. Proceso para crear el objeto de entrega

```mermaid
flowchart TD
    A["Interfaz llama crear_entrega(destino, distancia)"] --> B{"Tipo seleccionado"}
    B -- "Moto" --> C["Crear EntregaMoto"]
    B -- "Bicicleta" --> D["Crear EntregaBicicleta"]
    B -- "Carro" --> E["Crear EntregaCarro"]
    C --> F["Retornar objeto Entrega"]
    D --> F
    E --> F
```

### Explicacion

Aqui se aplica polimorfismo. La interfaz puede trabajar con cualquier objeto que herede de `Entrega`, sin importar si realmente es moto, bicicleta o carro.

## 5. Proceso para calcular tiempo

```mermaid
flowchart TD
    A["Se llama entrega.calcular_tiempo()"] --> B{"Tipo real del objeto"}
    B -- "EntregaMoto" --> C["Usar velocidad 40 km/h"]
    B -- "EntregaBicicleta" --> D["Usar velocidad 15 km/h"]
    B -- "EntregaCarro" --> E["Usar velocidad 30 km/h"]
    C --> F["tiempo = distancia / velocidad * 60"]
    D --> F
    E --> F
    F --> G["Redondear tiempo"]
    G --> H["Retornar minutos estimados"]
```

### Explicacion

Todos los tipos de entrega tienen el metodo `calcular_tiempo()`, pero cada clase usa una velocidad diferente. Por eso el resultado cambia segun el transporte.

## 6. Proceso para asignar repartidor

```mermaid
flowchart TD
    A["Se llama entrega.asignar_repartidor()"] --> B{"Tipo real del objeto"}
    B -- "EntregaMoto" --> C["Retornar Juan - Repartidor en Moto"]
    B -- "EntregaBicicleta" --> D["Retornar Pedro - Repartidor en Bicicleta"]
    B -- "EntregaCarro" --> E["Retornar Maria - Repartidora en Carro"]
```

### Explicacion

Este proceso tambien demuestra polimorfismo. El mismo metodo devuelve un repartidor distinto dependiendo de la clase del objeto.

## 7. Proceso para agregar entrega a la tabla

```mermaid
flowchart TD
    A["Entrega registrada correctamente"] --> B["Leer tipo de clase"]
    B --> C["Leer destino"]
    C --> D["Leer distancia"]
    D --> E["Llamar asignar_repartidor()"]
    E --> F["Llamar calcular_tiempo()"]
    F --> G["Insertar fila en Treeview"]
```

### Explicacion

La tabla muestra datos que vienen directamente del objeto creado. Para completar la fila, llama metodos del objeto como `asignar_repartidor()` y `calcular_tiempo()`.

## 8. Proceso para ver entregas registradas

```mermaid
flowchart TD
    A["Usuario presiona Ver entregas"] --> B["Limpiar mensajes anteriores"]
    B --> C{"Hay entregas registradas?"}
    C -- "No" --> D["Mostrar: No hay entregas registradas"]
    C -- "Si" --> E["Mostrar nombre de la plataforma"]
    E --> F["Recorrer lista plataforma.entregas"]
    F --> G["Mostrar tipo, destino y tiempo de cada entrega"]
```

### Explicacion

La plataforma guarda todas las entregas en una lista. Al presionar `Ver entregas`, la interfaz recorre esa lista y muestra un resumen textual.

## 9. Proceso para limpiar campos

```mermaid
flowchart TD
    A["Entrega registrada"] --> B["Borrar campo destino"]
    B --> C["Borrar campo distancia"]
    C --> D["Restablecer tipo de entrega a Moto"]
```

### Explicacion

Despues de registrar una entrega, la interfaz limpia los campos para que el usuario pueda ingresar otra entrega rapidamente.

## 10. Conceptos POO usados

| Concepto | Donde aparece | Explicacion |
| --- | --- | --- |
| Clase | `EntregaMoto`, `EntregaBicicleta`, `EntregaCarro` | Molde para crear entregas. |
| Objeto | `EntregaMoto(destino, distancia)` | Entrega concreta creada desde una clase. |
| Atributo | `destino`, `distancia`, `entregas` | Dato guardado dentro de un objeto. |
| Metodo | `calcular_tiempo()` | Accion que pertenece a una clase. |
| Herencia | `EntregaMoto(Entrega)` | Una clase hija reutiliza estructura de la clase padre. |
| Abstraccion | `Entrega(ABC)` | Define una plantilla obligatoria para todas las entregas. |
| Polimorfismo | `calcular_tiempo()` y `asignar_repartidor()` | El mismo metodo cambia su resultado segun el tipo de entrega. |
| Encapsulamiento | `self.destino`, `self.plataforma` | Los datos se organizan dentro del objeto que los usa. |
| Composicion | `PlataformaDomicilios` contiene entregas | Un objeto administra una lista de otros objetos. |
