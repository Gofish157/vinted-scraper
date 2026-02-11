from sqlalchemy import MetaData, Table, Column, Float, Integer, DateTime, String, select, text
from .db import engine

metadata = MetaData()

items = Table(
    "items",
    metadata,
    Column("id", String, primary_key=True),
    Column("status", String),
    Column("name", String),
    Column("size", String),
    Column("likes", Integer),
    Column("price", Float),
    Column("upload_time", DateTime),
    Column("item_condition", Integer),
    Column("link", String)
)

metadata.create_all(engine)