from enum import Enum

from clases.excepciones import (
    ReservaInvalidaError,
    OperacionNoPermitidaError
)

from clases.logs import registrar_evento, registrar_error


class EstadoReserva(Enum):
    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    CANCELADA = "Cancelada"
    PROCESADA = "Procesada"


class Reserva:
    """Relaciona un cliente con un servicio y controla su estado."""

    _contador = 0

    def __init__(self, cliente, servicio, duracion, **parametros):

        if cliente is None or servicio is None:
            raise ReservaInvalidaError(
                "La reserva requiere un cliente y un servicio."
            )

        self._contador += 1
        self.__codigo = f"RES-{self._contador:04d}"

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__parametros = parametros

        self.__estado = EstadoReserva.PENDIENTE
        self.__costo = None

        servicio.validar_parametros(
            duracion=duracion,
            **parametros
        )

        registrar_evento(f"Reserva creada: {self.__codigo}")

    @property
    def codigo(self):
        return self.__codigo

    @property
    def estado(self):
        return self.__estado.value

    @property
    def costo(self):
        return self.__costo

    def confirmar(self, impuesto=0, descuento=0):

        if self.__estado != EstadoReserva.PENDIENTE:
            raise OperacionNoPermitidaError(
                "Solo se puede confirmar una reserva pendiente."
            )

        try:
            self.__costo = self.__servicio.calcular_costo(
                self.__duracion,
                impuesto,
                descuento,
                **self.__parametros
            )

            self.__estado = EstadoReserva.CONFIRMADA

            registrar_evento(
                f"Reserva confirmada: {self.__codigo}"
            )

            return self.__costo

        except Exception as error:
            registrar_error(
                f"Error al confirmar {self.__codigo}"
            )

            raise ReservaInvalidaError(
                "No se pudo confirmar la reserva."
            ) from error

    def cancelar(self):

        if self.__estado not in (
            EstadoReserva.PENDIENTE,
            EstadoReserva.CONFIRMADA
        ):
            raise OperacionNoPermitidaError(
                "La reserva no se puede cancelar en su estado actual."
            )

        self.__estado = EstadoReserva.CANCELADA

        registrar_evento(
            f"Reserva cancelada: {self.__codigo}"
        )

    def procesar(self):

        if self.__estado != EstadoReserva.CONFIRMADA:
            raise OperacionNoPermitidaError(
                "Solo se puede procesar una reserva confirmada."
            )

        self.__estado = EstadoReserva.PROCESADA

        registrar_evento(
            f"Reserva procesada: {self.__codigo}"
        )

    def mostrar_informacion(self):
        return (
            f"Codigo: {self.__codigo}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duracion: {self.__duracion}\n"
            f"Estado: {self.estado}\n"
            f"Costo: {self.__costo}"
        )
