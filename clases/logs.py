import logging
from pathlib import Path

RUTA_LOG = Path(__file__).resolve().parent.parent / "registros" / "software_fj.log"
RUTA_LOG.parent.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("SoftwareFJ")
logger.setLevel(logging.INFO)

if not logger.handlers:
    manejador = logging.FileHandler(RUTA_LOG, encoding="utf-8")

    formato = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    manejador.setFormatter(formato)
    logger.addHandler(manejador)


def registrar_evento(mensaje):
    logger.info(mensaje)


def registrar_error(mensaje):
    logger.exception(mensaje)


def registrar_advertencia(mensaje):
    logger.warning(mensaje)
