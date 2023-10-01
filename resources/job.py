from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.job import Job, job_list


class JobListResource(Resource):

    def get(self):
        """GET Method to fetch all jobs."""
        data = []

        for job in job_list:
            if job.is_published is True:
                data.append(job.data)

        return {"data": data}, HTTPStatus.OK
   
    def post(self):
        """POST Method to make job offer."""
        data = request.get_json()

        job = Job(     
            title=data["title"],
            description=data["description"],
            salary=data["salary"]  
        )
        job_list.append(job)
        
        return job.data, HTTPStatus.CREATED


class JobResource(Resource):

    def get(self, job_id):
        """GET Method to fetch job with specific ID"""
        job = next((job for job in job_list
                    if job.id is job_id and job.is_published is True), None)
        
        if job is None:
            return {"message": "job not found"}, HTTPStatus.NOT_FOUND

        return job.data, HTTPStatus.OK
