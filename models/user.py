from extensions import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from passlib.hash import pbkdf2_sha256


class User(db.Model):
    """Class for user information."""
    
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(200))
    jobs = db.relationship("Job", backref="user")

    @property
    def data(self):
        return {
            "id": self.id,
            "username": self.username
        }

    @classmethod
    def hash_password(cls, password):
        return pbkdf2_sha256.hash(password)
    
    @classmethod
    def verify_password(cls, password, hashed):
        return pbkdf2_sha256.verify(password, hashed)
    
    # Current Instance focused
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()