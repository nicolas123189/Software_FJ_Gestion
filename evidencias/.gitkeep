"""Pruebas automaticas sencillas del proyecto Software FJ."""

import unittest

from clases.cliente import Cliente
from clases.reserva_sala import ReservaSala
from clases.alquiler_equipos import AlquilerEquipos
from clases.asesoria import Asesoria
from clases.reserva import Reserva

from clases.excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError
)


class PruebasSoftwareFJ(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente(
            "1001",
            "Maria Perez",
            "maria@gmail.com",
            "3001234567"
        )

    def test_cliente_valido(self):
        self.assertEqual(
            self.cliente.nombre,
            "Maria Perez"
        )

    def test_correo_invalido(self):
        with self.assertRaises(DatosInvalidosError):
            Cliente(
                "1002",
                "Pedro Lopez",
                "correo-malo",
                "3001234567"
            )

    def test_sala_calcula_costo(self):
        sala = ReservaSala(
            "S1",
            "Sala A",
            50000,
            10
        )

        self.assertEqual(
            sala.calcular_costo(2),
            100000
        )

    def test_sala_supera_capacidad(self):
        sala = ReservaSala(
            "S2",
            "Sala B",
            50000,
            5
        )

        with self.assertRaises(DatosInvalidosError):
            sala.validar_parametros(
                duracion=1,
                personas=8
            )

    def test_servicio_no_disponible(self):
        sala = ReservaSala(
            "S3",
            "Sala C",
            50000,
            5,
            disponible=False
        )

        with self.assertRaises(ServicioNoDisponibleError):
            sala.validar_parametros(
                duracion=1,
                personas=2
            )

    def test_reserva_confirmada(self):
        asesoria = Asesoria(
            "A1",
            "Asesoria TI",
            80000,
            "Tecnologia",
            "Luis"
        )

        reserva = Reserva(
            self.cliente,
            asesoria,
            1
        )

        self.assertEqual(
            reserva.confirmar(),
            80000
        )

        self.assertEqual(
            reserva.estado,
            "Confirmada"
        )

    def test_alquiler_calculo(self):
        equipo = AlquilerEquipos(
            "E1",
            "Portatil",
            20000,
            3
        )

        self.assertEqual(
            equipo.calcular_costo(2, cantidad=2),
            80000
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
