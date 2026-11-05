
import re
from clases.entidad import Entidad


class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):

        # Validar identificacion
        if not str(identificacion).strip():
            raise ValueError("La identificacion es obligatoria.")

        # Validar nombre
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del cliente es obligatorio.")

        if len(nombre.strip()) < 3:
            raise ValueError("El nombre debe tener minimo 3 caracteres.")

        # Validar correo electronico
        patron_correo = r'^[\w.+-]+@[\w-]+\.[\w.-]+$'

        if not re.match(patron_correo, correo):
            raise ValueError("El correo electronico no es valido.")

        # Validar telefono
        if not str(telefono).isdigit() or not (7 <= len(str(telefono)) <= 15):
            raise ValueError("El telefono debe tener entre 7 y 15 digitos.")

        # Inicializar la clase padre
        super().__init__(str(identificacion).strip())

        # Atributos encapsulados
        self.__nombre = nombre.strip()
        self.__correo = correo.strip().lower()
        self.__telefono = str(telefono)

    # Consultar nombre
    @property
    def nombre(self):
        return self.__nombre

    # Consultar correo
    @property
    def correo(self):
        return self.__correo

    # Consultar telefono
    @property
    def telefono(self):
        return self.__telefono

    # Actualizar correo con validacion
    def actualizar_correo(self, nuevo_correo):

        patron_correo = r'^[\w.+-]+@[\w-]+\.[\w.-]+$'

        if not re.match(patron_correo, nuevo_correo):
            raise ValueError("El nuevo correo no es valido.")

        self.__correo = nuevo_correo.strip().lower()

    # Mostrar informacion del cliente
    def mostrar_informacion(self):

        return (
            f"Identificacion: {self._identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )
