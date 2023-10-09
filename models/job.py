from extensions import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

job_list = []


def get_last_id():
    last_job = 1

    if job_list:
        last_job = job_list[-1].id + 1

    return last_job


class Job(db.Model):
    """Model class for job properties."""
    __tablename__ = "job"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    salary: Mapped[int] = mapped_column(Integer)
    is_published = db.Column(db.Boolean(), default=False)
    
    @property
    def data(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "salary": self.salary
        }
    
    # Save current object instance
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    # Delete current object instance
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(is_published=True).all()