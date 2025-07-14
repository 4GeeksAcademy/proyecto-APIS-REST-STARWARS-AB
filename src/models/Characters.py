
from sqlalchemy import ForeignKey, String, Boolean,Integer
from sqlalchemy.orm import Mapped, mapped_column,relationship
from database.db import db

from models.Planets import Planet


class Character(db.Model):
    __tablename__ = "character"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120),nullable=False)
    description:Mapped[str] = mapped_column(String(300),nullable=False)
    planet_id: Mapped[int] = mapped_column(Integer, ForeignKey("planet.id"))
    planet: Mapped["Planet"] =  relationship("Planet")
   


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "planet_id": self.planet_id


           
            
       }
