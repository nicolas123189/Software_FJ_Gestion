import re
from clases.entidad import Entidad
from clases.excepciones import DatosInvalidosError
from clases.logs import registrar_evento, registrar_error


class Cliente(Entidad):
    """Representa a una persona que utiliza los servicios de Software FJ."""

    def __init__(self, identificacion, nombre, correo, telefono):
        try:
            identificacion = str(identificacion).strip()
            nombre = str(nombre).strip()
            correo = str(correo).strip().lower()
            telefono = str(telefono).strip()

            if not identificacion:
                raise DatosInvalidosError("La identificacion es obligatoria.")

            if len(nombre) < 3:
                raise DatosInvalidosError(
                    "El nombre debe tener al menos 3 caracteres."
                )

            if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", correo):
                raise DatosInvalidosError(
                    "El correo electronico no es valido."
                )

            if not telefono.isdigit() or not 7 <= len(telefono) <= 15:
                raise DatosInvalidosError(
                    "El telefono debe tener entre 7 y 15 digitos."
                )

            super().__init__(identificacion)

            self.__nombre = nombre
            self.__correo = correo
            self.__telefono = telefono

            registrar_evento(f"Cliente creado: {identificacion}")

        except DatosInvalidosError:
            registrar_error("No fue posible crear el cliente.")
            raise

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def actualizar_correo(self, nuevo_correo):
        nuevo_correo = str(nuevo_correo).strip().lower()

        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", nuevo_correo):
            raise DatosInvalidosError("El nuevo correo no es valido.")

        self.__correo = nuevo_correo

        registrar_evento(
            f"Correo actualizado para cliente {self.identificador}"
        )

    def mostrar_informacion(self):
        return (
            f"Identificacion: {self.identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )
