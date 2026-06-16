# Diagrama UML y procesos - Universidad Virtual

Este documento explica la estructura del programa y los procesos principales de la aplicacion.

## 1. Diagrama UML de clases

```mermaid
classDiagram
    class ABC

    class Usuario {
        <<abstract>>
        +str nombre
        +str correo
        +__init__(nombre, correo)
        +iniciar_sesion() void
        +mostrar_permisos()* void
    }

    class Estudiante {
        +str carrera
        +__init__(nombre, correo, carrera)
        +mostrar_permisos() void
        +__str__() str
    }

    class Profesor {
        +str especialidad
        +__init__(nombre, correo, especialidad)
        +mostrar_permisos() void
        +__str__() str
    }

    class Curso {
        +str nombre
        +Profesor profesor
        +list~Estudiante~ estudiantes
        +__init__(nombre, profesor)
        +inscribir_estudiante(estudiante) bool
        +mostrar_info() void
    }

    class UniversidadVirtual {
        +str nombre
        +list~Usuario~ usuarios
        +list~Curso~ cursos
        +__init__(nombre)
        +agregar_usuario(usuario) void
        +agregar_curso(curso) void
        +mostrar_datos() void
    }

    class InterfazUniversidad {
        +Tk ventana
        +UniversidadVirtual universidad
        +list estudiantes
        +list profesores
        +crear_componentes() void
        +agregar_estudiante() void
        +agregar_profesor() void
        +crear_curso() void
        +inscribir_estudiante() void
        +ver_permisos() void
        +ver_resumen() void
    }

    ABC <|-- Usuario
    Usuario <|-- Estudiante
    Usuario <|-- Profesor
    UniversidadVirtual o-- Usuario : registra
    UniversidadVirtual o-- Curso : contiene
    Curso --> Profesor : asigna
    Curso o-- Estudiante : inscribe
    InterfazUniversidad --> UniversidadVirtual : administra
    InterfazUniversidad --> Estudiante : crea
    InterfazUniversidad --> Profesor : crea
    InterfazUniversidad --> Curso : crea
```

### Explicacion del UML

- `Usuario` es una clase abstracta: funciona como plantilla para usuarios concretos.
- `Estudiante` y `Profesor` heredan de `Usuario`, por eso reutilizan `nombre`, `correo` e `iniciar_sesion()`.
- `mostrar_permisos()` aplica polimorfismo: cada clase hija implementa permisos diferentes.
- `Curso` se relaciona con un `Profesor` y contiene una lista de `Estudiante`.
- `UniversidadVirtual` administra usuarios y cursos.
- `InterfazUniversidad` usa las clases anteriores para mostrar una interfaz grafica.

## 2. Proceso para agregar un estudiante

```mermaid
flowchart TD
    A["Usuario escribe nombre, correo y carrera"] --> B["Presiona Agregar estudiante"]
    B --> C{"Los campos estan completos?"}
    C -- "No" --> D["Mostrar advertencia"]
    C -- "Si" --> E["Crear objeto Estudiante"]
    E --> F["Guardar estudiante en la lista de la interfaz"]
    F --> G["Agregar estudiante a UniversidadVirtual.usuarios"]
    G --> H["Mostrar estudiante en la lista visual"]
    H --> I["Mostrar mensaje de confirmacion"]
```

### Explicacion

La interfaz toma los datos escritos, valida que no esten vacios y crea un objeto `Estudiante`. Luego ese objeto se guarda tanto en la interfaz como en la universidad.

## 3. Proceso para agregar un profesor

```mermaid
flowchart TD
    A["Usuario escribe nombre, correo y especialidad"] --> B["Presiona Agregar profesor"]
    B --> C{"Los campos estan completos?"}
    C -- "No" --> D["Mostrar advertencia"]
    C -- "Si" --> E["Crear objeto Profesor"]
    E --> F["Guardar profesor en la lista de la interfaz"]
    F --> G["Agregar profesor a UniversidadVirtual.usuarios"]
    G --> H["Mostrar profesor en la lista visual"]
    H --> I["Mostrar mensaje de confirmacion"]
```

### Explicacion

Este proceso es parecido al del estudiante, pero crea un objeto `Profesor`. La especialidad reemplaza a la carrera.

## 4. Proceso para crear un curso

```mermaid
flowchart TD
    A["Usuario escribe nombre del curso"] --> B["Selecciona un profesor"]
    B --> C["Presiona Crear curso"]
    C --> D{"Curso y profesor validos?"}
    D -- "No" --> E["Mostrar advertencia"]
    D -- "Si" --> F["Crear objeto Curso"]
    F --> G["Asignar profesor al curso"]
    G --> H["Agregar curso a UniversidadVirtual.cursos"]
    H --> I["Mostrar curso en la lista visual"]
    I --> J["Mostrar mensaje de confirmacion"]
```

### Explicacion

Para crear un curso se necesita un nombre y un profesor. El curso queda asociado al profesor seleccionado.

## 5. Proceso para inscribir estudiante en curso

```mermaid
flowchart TD
    A["Usuario selecciona un estudiante"] --> B["Usuario selecciona un curso"]
    B --> C["Presiona Inscribir estudiante"]
    C --> D{"Hay estudiante y curso seleccionados?"}
    D -- "No" --> E["Mostrar advertencia"]
    D -- "Si" --> F["Llamar curso.inscribir_estudiante(estudiante)"]
    F --> G{"El estudiante ya estaba inscrito?"}
    G -- "Si" --> H["Mostrar mensaje: ya esta inscrito"]
    G -- "No" --> I["Agregar estudiante a curso.estudiantes"]
    I --> J["Mostrar mensaje: inscripcion exitosa"]
```

### Explicacion

El metodo `inscribir_estudiante()` evita duplicados. Si el estudiante ya existe dentro del curso, no lo vuelve a agregar.

## 6. Proceso para ver permisos

```mermaid
flowchart TD
    A["Usuario selecciona estudiante o profesor"] --> B["Presiona Ver permisos"]
    B --> C{"Hay usuario seleccionado?"}
    C -- "No" --> D["Mostrar advertencia"]
    C -- "Si" --> E["Llamar usuario.mostrar_permisos()"]
    E --> F{"Tipo de usuario"}
    F -- "Estudiante" --> G["Mostrar permisos de estudiante"]
    F -- "Profesor" --> H["Mostrar permisos de profesor"]
```

### Explicacion

Aqui se ve el polimorfismo: la interfaz llama el mismo metodo `mostrar_permisos()`, pero la respuesta cambia segun si el objeto es `Estudiante` o `Profesor`.

## 7. Proceso para ver resumen

```mermaid
flowchart TD
    A["Usuario presiona Ver resumen"] --> B["Limpiar salida anterior"]
    B --> C["Llamar universidad.mostrar_datos()"]
    C --> D["Mostrar usuarios registrados"]
    D --> E["Mostrar cursos disponibles"]
    E --> F["Recorrer cada curso"]
    F --> G["Llamar curso.mostrar_info()"]
    G --> H["Mostrar profesor y estudiantes inscritos"]
```

### Explicacion

El resumen consulta los objetos guardados en `UniversidadVirtual` y en cada `Curso`. No crea datos nuevos, solo muestra el estado actual del sistema.

## 8. Conceptos POO usados

| Concepto | Donde aparece | Explicacion |
| --- | --- | --- |
| Clase | `Estudiante`, `Profesor`, `Curso` | Molde para crear objetos. |
| Objeto | `estudiante = Estudiante(...)` | Instancia real creada desde una clase. |
| Atributo | `nombre`, `correo`, `carrera` | Dato guardado dentro del objeto. |
| Metodo | `mostrar_permisos()` | Funcion que pertenece a una clase. |
| Herencia | `Estudiante(Usuario)` | Una clase hija reutiliza codigo de una clase padre. |
| Abstraccion | `Usuario(ABC)` | Define una plantilla general sin crear usuarios genericos. |
| Polimorfismo | `mostrar_permisos()` | El mismo metodo tiene comportamiento distinto segun la clase. |
| Composicion | `Curso` contiene estudiantes | Un objeto esta formado o relacionado con otros objetos. |
| Encapsulamiento | `self.nombre`, `self.cursos` | Los datos se agrupan dentro del objeto que los usa. |
