from clases.servicio import Servicio
from clases.excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError
)


class AlquilerEquipos(Servicio):

    def __init__(self, identificador, nombre, precio_base, unidades_disponibles):
        super().__init__(identificador, nombre, precio_base)

        if not isinstance(unidades_disponibles, int) or unidades_disponibles < 0:
            raise DatosInvalidosError(
                "Las unidades disponibles deben ser un entero no negativo."
            )

        self._unidades_disponibles = unidades_disponibles

    @property
    def unidades_disponibles(self):
        return self._unidades_disponibles

    def validar_parametros(self, **kwargs):
        duracion = kwargs.get("duracion")
        cantidad = kwargs.get("cantidad", 1)

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatosInvalidosError(
                "La duracion del alquiler debe ser mayor que cero."
            )

        if not isinstance(cantidad, int) or cantidad <= 0:
            raise DatosInvalidosError(
                "La cantidad debe ser un entero positivo."
            )

        if cantidad > self._unidades_disponibles:
            raise ServicioNoDisponibleError(
                "No hay suficientes equipos disponibles."
            )

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0, cantidad=1):
        self.validar_parametros(
            duracion=duracion,
            cantidad=cantidad
        )

        subtotal = self.precio_base * duracion * cantidad

        if not 0 <= impuesto <= 100 or not 0 <= descuento <= 100:
            raise DatosInvalidosError(
                "Impuesto y descuento deben estar entre 0 y 100."
            )

        total = subtotal * (1 + impuesto / 100) * (1 - descuento / 100)

        return round(total, 2)

    def reservar_unidades(self, cantidad):
        self.validar_parametros(
            duracion=1,
            cantidad=cantidad
        )

        self._unidades_disponibles -= cantidad

    def describir_servicio(self):
        return (
            f"{self.nombre} | Precio por hora y unidad: "
            f"${self.precio_base:,.2f} | "
            f"Unidades disponibles: {self._unidades_disponibles}"
        )
