from celery import shared_task
from backend.src.tiendamiaus.services import TiendamiausService
from backend.src.worten.services import WortenService
import logging

@shared_task
def import_orders():
    logging.info("Importing orders...")

    tiendamiaus = TiendamiausService()
    tiendamiaus.get_orders()

    worten = WortenService()
    worten.get_orders()

    return "Orders imported successfully!"