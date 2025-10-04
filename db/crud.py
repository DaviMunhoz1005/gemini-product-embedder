from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import SQLAlchemyError

from utils.logger_config import setup_logger

logger = setup_logger(__name__)

def insert_product(conn, products_table, product_data):
    stmt = insert(products_table).values(product_data)
    stmt = stmt.on_conflict_do_nothing(
        index_elements=["name", "description"]
    ).returning(products_table.c.id)

    try:
        result = conn.execute(stmt).first()
        return result
    except SQLAlchemyError as e:
        print(f"Error inserting '{product_data['name']}':", e)
        return None

def product_exists(conn, products_table, name, description):
    stmt = select(products_table.c.id).where(
        products_table.c.name == name,
        products_table.c.description == description
    )
    return conn.execute(stmt).first() is not None
