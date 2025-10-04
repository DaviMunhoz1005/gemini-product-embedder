from sqlalchemy import Table, Column, String, Float, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from pgvector.sqlalchemy import Vector
import uuid
from db.connection import metadata, engine
from utils.logger_config import setup_logger

logger = setup_logger(__name__)

def create_products_table():
    logger.info("Checking or creating 'Products' table ...")
    products_table = Table(
        "products",
        metadata,
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("name", String, nullable=False),
        Column("description", String, nullable=True),
        Column("price", Float, nullable=False),
        Column("tags", ARRAY(String), nullable=False),
        Column("allergenic", ARRAY(String), nullable=False),
        Column("type", String, nullable=False),
        Column("fits_people", Float, nullable=False),
        Column("embedding", Vector(3072), nullable=False),
        UniqueConstraint("name", "description", name="uq_name_description")
    )
    metadata.create_all(engine)
    return products_table
