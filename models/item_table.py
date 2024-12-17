from sqlalchemy import Column, Integer, String, Float, Boolean
from db.connection import Base

class ItemDB(Base):
    __tablename__ = "items_data"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable = True)
    price = Column(Float, nullable= False)
    on_offer = Column(Boolean, nullable=False, default=False)