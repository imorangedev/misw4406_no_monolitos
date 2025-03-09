from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from dominio.schema import CompilationModel
from seedwork.logger_config import get_logger

class CompilationRepository:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.logger = get_logger("COMPILATION_REPOSITORY")

    def find_by_property(self, property_name: str, value):
        try:
            with self.SessionLocal() as session:
                return session.query(CompilationModel).filter(getattr(CompilationModel, property_name) == value).all()
        except AttributeError:
            self.logger.error(f"Invalid property name: {property_name}")
        except SQLAlchemyError as e:
            self.logger.error(f"Database error: {str(e)}")


