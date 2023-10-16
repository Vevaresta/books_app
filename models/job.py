import logging
from extensions import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


logger = logging.getLogger("server_log")


class Job(db.Model):
    """Model class for job properties."""
    __tablename__ = "job"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    salary: Mapped[int] = mapped_column(Integer)
    is_published = db.Column(db.Boolean(), default=False)
    
    @property
    def data(self):
        logger.info("Data accessed for a Job with an ID: %s", self.id)
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "salary": self.salary
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        logger.info("Job saved: %s", self.title)
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        logger.info("Job deleted: %s", self.title)

    @classmethod
    def get_all_published(cls):
        jobs = cls.query.filter_by(is_published=True).all()
        logger.info("Fetched all published jobs.")
        return jobs
    
    @classmethod
    def get_by_id(cls, job_id):
        job = cls.query.filter_by(id=job_id).first()
        logger.info("Fetched job by ID: %s", job_id)       
        return job