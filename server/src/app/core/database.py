from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

from .config import settings

engine = create_engine(settings.DATA_SOURCE, echo=settings.DEBUG)
SessionLocal = sessionmaker(bind=engine)

def get_data_base():
    data_base = SessionLocal()
    try:
        yield data_base
    except Exception as error:
        data_base.rollback()
        logging.error(
            "Error en la conexión con la Db ",
            error
        )
    finally:
        data_base.close()
        
        
    