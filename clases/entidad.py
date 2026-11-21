from abc import ABC, abstractmethod


class Entidad(ABC):
    """Clase abstracta general para las entidades del sistema."""

    def __init__(self, identificador):
        identificador = str(identificador).strip()

        if not identificador:
            raise ValueError("El identificador es obligatorio.")

        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def mostrar_informacion(self):
        """Cada entidad debe definir como muestra su informacion."""
        raise NotImplementedError
