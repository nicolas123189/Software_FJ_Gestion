from clases.servicio import Servicio
from clases.excepciones import DatosInvalidosError


class Asesoria(Servicio):

    def __init__(self, identificador, nombre, precio_base, especialidad, asesor):
        super().__init__(identificador, nombre, precio_base)

        if not str(especialidad).strip() or not str(asesor).strip():
            raise DatosInvalidosError(
                "La especialidad y el asesor son obligatorios."
            )

        self._especialidad = especialidad.strip()
        self._asesor = asesor.strip()

    def validar_parametros(self, **kwargs):
        duracion = kwargs.get("duracion")

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatosInvalidosError(
                "La duracion de la asesoria debe ser mayor que cero."
            )

        return True

    def describir_servicio(self):
        return (
            f"{self.nombre} | Especialidad: {self._especialidad} | "
            f"Asesor: {self._asesor} | "
            f"Precio por hora: ${self.precio_base:,.2f}"
        )
