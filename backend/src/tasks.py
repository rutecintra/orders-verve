from celery import shared_task
from src.services.tiendamiaus_service import fetch_orders_from_api

@shared_task
def sync_orders_task():
    fetch_orders_from_api()
    return "Sincronização de pedidos concluída!"