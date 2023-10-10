from extensions import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class User(db.Model):
    """Class for user information."""
    
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(200))
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()