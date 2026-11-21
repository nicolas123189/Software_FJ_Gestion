from abc import ABC, abstractmethod
from clases.excepciones import DatosInvalidosError


class Servicio(ABC):
    """Clase abstracta base para todos los servicios."""

    def __init__(self, identificador, nombre, precio_base):

        if not str(identificador).strip():
            raise DatosInvalidosError(
                "El identificador del servicio es obligatorio."
            )

        if not str(nombre).strip():
            raise DatosInvalidosError(
                "El nombre del servicio es obligatorio."
            )

        if not isinstance(precio_base, (int, float)) or precio_base < 0:
            raise DatosInvalidosError(
                "El precio base debe ser un numero no negativo."
            )

        self._identificador = str(identificador).strip()
        self._nombre = str(nombre).strip()
        self._precio_base = float(precio_base)

    @property
    def identificador(self):
        return self._identificador

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @abstractmethod
    def validar_parametros(self, **kwargs):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """
        Permite calcular el costo con diferentes parametros:
        calcular_costo(duracion)
        calcular_costo(duracion, impuesto)
        calcular_costo(duracion, impuesto, descuento)
        """

        self.validar_parametros(duracion=duracion)

        if not 0 <= impuesto <= 100 or not 0 <= descuento <= 100:
            raise DatosInvalidosError(
                "Impuesto y descuento deben estar entre 0 y 100."
            )

        subtotal = self.precio_base * duracion
        total = subtotal + subtotal * impuesto / 100
        total -= total * descuento / 100

        return round(total, 2)
