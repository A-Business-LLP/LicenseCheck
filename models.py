from sqlalchemy import Date, String, Boolean, Integer, create_engine
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from sqlalchemy import MetaData
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date, datetime


metadata_obj = MetaData()


class Base(DeclarativeBase):
    metadata = metadata_obj


class Robot(Base):
    __tablename__ = "robot_account"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    license_end_date: Mapped[date] = mapped_column(Date, nullable=False) 

    def __init__(self, name: str, license_end_date: date):
        self.name = name
        self.license_end_date = license_end_date

    @hybrid_property
    def status(self) -> bool:
        return self.license_end_date >= datetime.now().date()

    def __repr__(self) -> str:
        return f"Robot(id={self.id!r}, name={self.name!r}, license_end_date={self.license_end_date!r}, status={self.status!r})"
