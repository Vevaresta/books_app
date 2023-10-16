from extensions import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from passlib.hash import pbkdf2_sha256
import logging


logger = logging.getLogger("server_log")


class User(db.Model):
    """Class for user information."""
    
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(200))
    jobs = db.relationship("Job", backref="user")

    @property
    def data(self):
        logger.info("Data accessed for a User with an ID: %s", self.id)
        return {
            "id": self.id,
            "username": self.username
        }

    @classmethod
    def hash_password(cls, password):
        logger.info("Hashing password...")
        hashed_password = pbkdf2_sha256.hash(password)
        logger.info("Password hashed successfully.")
        return hashed_password
    
    @classmethod
    def verify_password(cls, password, hashed):
        logger.info("Verifying password...")
        verified_password = pbkdf2_sha256.verify(password, hashed)
        logger.info("Password verified.")
        return verified_password
    
    # Current Instance focused
    def save(self):
        db.session.add(self)
        db.session.commit()
        logger.info("User saved: %s", self.username)
    
    @classmethod
    def get_by_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        logger.info("Fetched username: %s", username)  
        return user