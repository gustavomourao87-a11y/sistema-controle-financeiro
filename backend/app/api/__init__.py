from .database.tables import create_tables


def initialize_database():
    create_tables()