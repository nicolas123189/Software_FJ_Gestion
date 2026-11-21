from clases.servicio import Servicio
from clases.excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError
)


class ReservaSala(Servicio):

    def __init__(self, identificador, nombre, precio_base, capacidad, disponible=True):
        super().__init__(identificador, nombre, precio_base)

        if not isinstance(capacidad, int) or capacidad <= 0:
            raise DatosInvalidosError(
                "La capacidad debe ser un entero mayor que cero."
            )

        self._capacidad = capacidad
        self._disponible = bool(disponible)

    @property
    def capacidad(self):
        return self._capacidad

    def verificar_disponibilidad(self):
        return self._disponible

    def cambiar_disponibilidad(self, disponible):
        self._disponible = bool(disponible)

    def validar_parametros(self, **kwargs):
        duracion = kwargs.get("duracion")
        personas = kwargs.get("personas", 1)

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatosInvalidosError(
                "La duracion debe ser mayor que cero."
            )

        if not isinstance(personas, int) or personas <= 0:
            raise DatosInvalidosError(
                "La cantidad de personas debe ser un entero positivo."
            )

        if personas > self._capacidad:
            raise DatosInvalidosError(
                "La cantidad de personas supera la capacidad de la sala."
            )

        if not self._disponible:
            raise ServicioNoDisponibleError(
                "La sala no esta disponible."
            )

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0, personas=1):
        self.validar_parametros(
            duracion=duracion,
            personas=personas
        )

        return super().calcular_costo(
            duracion,
            impuesto,
            descuento
        )

    def describir_servicio(self):
        estado = "Disponible" if self._disponible else "No disponible"

        return (
            f"{self.nombre} | Capacidad: {self._capacidad} personas | "
            f"Precio por hora: ${self.precio_base:,.2f} | {estado}"
        )
