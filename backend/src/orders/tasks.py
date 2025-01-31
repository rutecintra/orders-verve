from celery import shared_task
from src.miraklintegration.services.tiendamiaus_service import TiendamiausService
from src.miraklintegration.services.worten_service import WortenService
import logging

@shared_task
def import_orders():
    logging.info("Importing orders...")

    tiendamiaus = TiendamiausService()
    tiendamiaus.get_orders()

    worten = WortenService()
    worten.get_orders()

    return "Orders imported successfully!"