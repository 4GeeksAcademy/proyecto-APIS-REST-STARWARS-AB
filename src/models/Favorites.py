from sqlalchemy import String,Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from database.db import db
from models.Characters import Character
from models.Planets import Planet
from models.User import User



class Favorite(db.Model):
    __tablename__="favorite"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"),nullable= False)
    planet_id: Mapped[int] = mapped_column(Integer, ForeignKey("planet.id"),nullable=True)
    character_id: Mapped[int] = mapped_column(Integer, ForeignKey("character.id"),nullable=True)
  
    

    

    user: Mapped["User"] = relationship("User", back_populates = "favorites")
    planet: Mapped["Planet"] = relationship("Planet")
    character: Mapped["Character"] = relationship("Character")
 