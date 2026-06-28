# Caso 18 - Sistema de autenticacion

## Diagrama UML

```mermaid
classDiagram
    class Autenticacion {
        <<abstract>>
        +login()
        +logout()
    }

    class LoginGoogle
    class LoginFacebook
    class LoginGitHub

    Autenticacion <|-- LoginGoogle
    Autenticacion <|-- LoginFacebook
    Autenticacion <|-- LoginGitHub
```

## Proceso

```mermaid
flowchart TD
    A["Usuario elige login"] --> B{"Proveedor"}
    B --> C["LoginGoogle"]
    B --> D["LoginFacebook"]
    B --> E["LoginGitHub"]
    C --> F["login()"]
    D --> F
    E --> F
    F --> G["Acceder a la aplicacion"]
    G --> H["logout()"]
```

## Explicacion

`Autenticacion` define entrada y salida del sistema. Cada proveedor implementa su propia forma de iniciar sesion.
