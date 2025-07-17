from sqlalchemy import ForeignKey, String,Integer
from sqlalchemy.orm import Mapped, mapped_column,relationship
from database.db import db
from models.Characters import Character
from models.Planets import Planet




class User(db.Model):
    __tablename__ ="user"
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    nickname: Mapped[str] = mapped_column(String(120),nullable=False)
    favorites: Mapped[list["Favorite"]] =  relationship("Favorite",back_populates="user")
    


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "nickname": self.nickname,
            "favorites":[ fav.serialize() for fav in self.favorites ]
            
            
        }
    
class Favorite(db.Model):
    __tablename__="favorite"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"),nullable= False)
    planet_id: Mapped[int] = mapped_column(Integer, ForeignKey("planet.id"),nullable=True)
    character_id: Mapped[int] = mapped_column(Integer, ForeignKey("character.id"),nullable=True)
    user: Mapped["User"] = relationship("User", back_populates = "favorites")
    planet: Mapped["Planet"] = relationship("Planet")
    character: Mapped["Character"] = relationship("Character")
    
    def serialize(self):
        return{
        "id": self.id,
        "user_id": self.user_id,
        "planet_id":self.planet_id,
        "character_id":self.character_id
       

        }
        
