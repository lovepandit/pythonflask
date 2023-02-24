import logging
from flask import Blueprint
from models.response import Response
logger = logging.getLogger("flask-app")
from services.products_service import get_all_products

admin_blueprint = Blueprint("admin", __name__)

@admin_blueprint.route('/products', methods=['GET'])
def all_products():
    logger.info("Get admin products.")
    products = get_all_products()
    logger.debug("Retrieved products success.")
    resp = Response(True, "All products.", products)
    return resp.to_dict()