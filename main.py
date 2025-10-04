from db.connection import engine
from db.models import create_products_table
from db.crud import insert_product, product_exists
from embeddings.generate import generate_embedding
from utils.read_json_products import get_products_from_json
from utils.logger_config import setup_logger
import uuid

"""
    É necessário criar a extensão vector para criar vetores embeddings com pgvector
    Rode o seguinte comando no Database
    CREATE EXTENSION IF NOT EXISTS vector;
"""

logger = setup_logger(__name__)
path_json = "./data/products.json"

logger.info("Establishing connection with the DB ...")
products_table = create_products_table()
logger.info(f"Taking '{path_json}' products")
products = get_products_from_json(f"{path_json}")

with engine.begin() as conn:
    for product in products:
        if product_exists(conn, products_table, product.get("name"), product.get("description")):
            logger.info(f"'{product.get("name")}' already exists. Skipping...")
            continue
        logger.info(f"Generating embedding for '{product.get('name')}' ...")
        fields = ["name", "description", "price", "tags", "allergenic", "type", "fits_people"]
        text_to_embed = " ".join(str(product.get(field, "")) for field in fields)
        embedding = generate_embedding(text_to_embed)
        product_data = {
            "id": uuid.uuid4(),
            "name": product.get("name"),
            "description": product.get("description"),
            "price": product.get("price"),
            "tags": product.get("tags", []),
            "allergenic": product.get("allergenic", []),
            "type": product.get("type"),
            "fits_people": product.get("fits_people"),
            "embedding": embedding
        }
        result = insert_product(conn, products_table, product_data)
        logger.info(f"'{product.get("name")}' inserted successfully!")

logger.info("Successful product insertion!")