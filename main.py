from clases.cliente import Cliente
from clases.reserva_sala import ReservaSala
from clases.alquiler_equipos import AlquilerEquipos
from clases.asesoria import Asesoria
from clases.reserva import Reserva
from clases.logs import registrar_evento, registrar_error


class SistemaSoftwareFJ:
    """Administra los objetos en listas, sin utilizar bases de datos."""

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        if any(
            c.identificador == cliente.identificador
            for c in self.clientes
        ):
            raise ValueError(
                "Ya existe un cliente con esa identificacion."
            )

        self.clientes.append(cliente)

        registrar_evento(
            f"Cliente agregado al sistema: {cliente.identificador}"
        )

    def agregar_servicio(self, servicio):
        if any(
            s.identificador == servicio.identificador
            for s in self.servicios
        ):
            raise ValueError(
                "Ya existe un servicio con ese identificador."
            )

        self.servicios.append(servicio)

        registrar_evento(
            f"Servicio agregado: {servicio.identificador}"
        )

    def crear_reserva(self, cliente, servicio, duracion, **parametros):
        reserva = Reserva(
            cliente,
            servicio,
            duracion,
            **parametros
        )

        self.reservas.append(reserva)

        return reserva

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente.mostrar_informacion(), "\n")

    def listar_servicios(self):
        for servicio in self.servicios:
            print(servicio.describir_servicio())


def ejecutar_demostracion():

    sistema = SistemaSoftwareFJ()

    print("\n===== SISTEMA SOFTWARE FJ: DEMOSTRACION =====")

    # 1. Registrar cliente valido.
    try:
        cliente = Cliente(
            "123456789",
            "Carlos Ramirez",
            "carlos@gmail.com",
            "3001234567"
        )

        sistema.registrar_cliente(cliente)

        print("1. Cliente registrado correctamente.")

    except Exception as error:
        registrar_error("Operacion 1: registro de cliente")
        print("1. Error:", error)

    # 2. Intentar registrar cliente con correo invalido.
    try:
        Cliente(
            "222",
            "Ana Lopez",
            "correo-no-valido",
            "3101234567"
        )

    except Exception as error:
        registrar_error("Operacion 2: cliente invalido")
        print("2. Cliente invalido controlado:", error)

    # 3. Crear servicio de sala.
    try:
        sala = ReservaSala(
            "S01",
            "Sala de reuniones",
            50000,
            capacidad=12
        )

        sistema.agregar_servicio(sala)

        print("3. Servicio de sala creado.")

    except Exception as error:
        registrar_error("Operacion 3: creacion de sala")
        print("3. Error:", error)

    # 4. Crear alquiler de equipos.
    try:
        equipos = AlquilerEquipos(
            "E01",
            "Video beam",
            30000,
            unidades_disponibles=4
        )

        sistema.agregar_servicio(equipos)

        print("4. Servicio de alquiler creado.")

    except Exception as error:
        registrar_error("Operacion 4: creacion de equipos")
        print("4. Error:", error)

    # 5. Crear asesoria.
    try:
        asesoria = Asesoria(
            "A01",
            "Asesoria de software",
            80000,
            "Desarrollo de software",
            "Laura Gomez"
        )

        sistema.agregar_servicio(asesoria)

        print("5. Servicio de asesoria creado.")

    except Exception as error:
        registrar_error("Operacion 5: creacion de asesoria")
        print("5. Error:", error)

    # 6. Crear y confirmar reserva de sala.
    try:
        reserva1 = sistema.crear_reserva(
            cliente,
            sala,
            2,
            personas=8
        )

        costo = reserva1.confirmar(
            impuesto=19,
            descuento=5
        )

        print(
            f"6. Reserva de sala confirmada. Total: ${costo:,.2f}"
        )

    except Exception as error:
        registrar_error("Operacion 6: reserva de sala")
        print("6. Error:", error)

    # 7. Intentar reservar sala superando capacidad.
    try:
        sistema.crear_reserva(
            cliente,
            sala,
            2,
            personas=20
        )

    except Exception as error:
        registrar_error("Operacion 7: capacidad excedida")
        print("7. Reserva incorrecta controlada:", error)

    # 8. Crear y confirmar alquiler de dos equipos.
    try:
        reserva2 = sistema.crear_reserva(
            cliente,
            equipos,
            3,
            cantidad=2
        )

        costo = reserva2.confirmar()

        print(
            f"8. Alquiler confirmado. Total: ${costo:,.2f}"
        )

    except Exception as error:
        registrar_error("Operacion 8: alquiler de equipos")
        print("8. Error:", error)

    # 9. Intentar alquilar mas equipos de los disponibles.
    try:
        sistema.crear_reserva(
            cliente,
            equipos,
            2,
            cantidad=10
        )

    except Exception as error:
        registrar_error("Operacion 9: equipos insuficientes")
        print("9. Alquiler fallido controlado:", error)

    # 10. Crear, confirmar y procesar una asesoria.
    try:
        reserva3 = sistema.crear_reserva(
            cliente,
            asesoria,
            1.5
        )

        reserva3.confirmar(descuento=10)
        reserva3.procesar()

        print("10. Asesoria confirmada y procesada.")

    except Exception as error:
        registrar_error("Operacion 10: asesoria")
        print("10. Error:", error)

    # Ejemplo de try/except/else/finally.
    try:
        print(
            "\nResumen: clientes =", len(sistema.clientes),
            "| servicios =", len(sistema.servicios),
            "| reservas =", len(sistema.reservas)
        )

    except Exception as error:
        registrar_error("Error al mostrar resumen")
        print("No fue posible mostrar el resumen:", error)

    else:
        print("Resumen generado correctamente.")

    finally:
        print(
            "Demostracion finalizada. El sistema sigue disponible."
        )


def menu():

    sistema = SistemaSoftwareFJ()

    while True:

        print("\n===== SOFTWARE FJ =====")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Listar servicios de demostracion")
        print("4. Ejecutar las 10 operaciones de prueba")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        try:

            if opcion == "1":

                cliente = Cliente(
                    input("Identificacion: "),
                    input("Nombre: "),
                    input("Correo: "),
                    input("Telefono: ")
                )

                sistema.registrar_cliente(cliente)

                print("Cliente registrado.")

            elif opcion == "2":

                sistema.listar_clientes()

            elif opcion == "3":

                if not sistema.servicios:
                    print(
                        "No hay servicios registrados en esta sesion."
                    )
                else:
                    sistema.listar_servicios()

            elif opcion == "4":

                ejecutar_demostracion()

            elif opcion == "0":

                print("Hasta pronto.")
                break

            else:

                print("Opcion no valida.")

        except Exception as error:
            registrar_error("Error controlado en el menu")
            print("No se pudo completar la operacion:", error)

        finally:
            print("Operacion terminada.")


if __name__ == "__main__":
    ejecutar_demostracion()

    # Para utilizar el menu interactivo:
    # comenta la linea anterior y descomenta la siguiente:
    # menu()
