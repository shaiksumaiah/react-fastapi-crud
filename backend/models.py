from sqlalchemy import Column, Integer, String
from database import Base

# Item table with id, name, description
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)