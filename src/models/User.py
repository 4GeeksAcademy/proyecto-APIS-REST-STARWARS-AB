from sqlalchemy import String,Integer
from sqlalchemy.orm import Mapped, mapped_column,relationship
from database.db import db
from models.Favorites import Favorite




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
            
        }