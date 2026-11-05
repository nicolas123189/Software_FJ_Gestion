
from abc import ABC, abstractmethod


class Entidad(ABC):

    def __init__(self, identificador):
        self._identificador = identificador

    @abstractmethod
    def mostrar_informacion(self):
        pass
