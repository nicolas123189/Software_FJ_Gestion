class SoftwareFJError(Exception):
    """Excepcion base del sistema."""


class DatosInvalidosError(SoftwareFJError):
    """Se utiliza cuando los datos ingresados no cumplen las validaciones."""


class ServicioNoDisponibleError(SoftwareFJError):
    """Se utiliza cuando un servicio no esta disponible."""


class ReservaInvalidaError(SoftwareFJError):
    """Se utiliza cuando una reserva no puede procesarse."""


class OperacionNoPermitidaError(SoftwareFJError):
    """Se utiliza cuando se intenta realizar una operacion no permitida."""
