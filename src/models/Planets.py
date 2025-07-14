
from sqlalchemy import String,Integer
from sqlalchemy.orm import Mapped, mapped_column
from database.db import db



class Planet(db.Model):
    __tablename__ ="planet"
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    name: Mapped[str] = mapped_column(String(120),nullable=False)
    description:Mapped[str] = mapped_column(String(300),nullable=False)
    rotation: Mapped[int] = mapped_column(Integer,nullable = False)
    
   
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "rotation": self.rotation
       }