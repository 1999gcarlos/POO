from abc import ABC, abstractmethod


class Autenticacion(ABC):
    def __init__(self, usuario):
        self.usuario = usuario

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass


class LoginGoogle(Autenticacion):
    def login(self):
        return f"{self.usuario} inicio sesion con Google."

    def logout(self):
        return f"{self.usuario} cerro sesion de Google."


class LoginFacebook(Autenticacion):
    def login(self):
        return f"{self.usuario} inicio sesion con Facebook."

    def logout(self):
        return f"{self.usuario} cerro sesion de Facebook."


class LoginGitHub(Autenticacion):
    def login(self):
        return f"{self.usuario} inicio sesion con GitHub."

    def logout(self):
        return f"{self.usuario} cerro sesion de GitHub."


def main():
    logins = []

    while True:
        print("\n--- Sistema de autenticacion ---")
        print("1. Login con Google")
        print("2. Login con Facebook")
        print("3. Login con GitHub")
        print("4. Ver sesiones")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion in ["1", "2", "3"]:
            usuario = input("Usuario: ")
            if opcion == "1":
                login = LoginGoogle(usuario)
            elif opcion == "2":
                login = LoginFacebook(usuario)
            else:
                login = LoginGitHub(usuario)
            logins.append(login)
            print(login.login())

        elif opcion == "4":
            if not logins:
                print("No hay sesiones registradas.")
            for login in logins:
                print(login.logout())

        elif opcion == "5":
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
