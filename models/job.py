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
    is_published = Mapped[bool] 
