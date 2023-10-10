from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.job import Job


class JobListResource(Resource):

    def get(self):
        """GET Method to fetch all jobs."""
        job_data = []

        for job in Job.get_all_published():
            if job.is_published is True:
                job_data.append(job.data)

        return {"Available Jobs": job_data}, HTTPStatus.OK
   
    def post(self):
        """POST Method to make job offer."""
        data = request.get_json()

        job = Job(     
            title=data["title"],
            description=data["description"],
            salary=data["salary"]  
        )
        job.save()
        
        return job.data, HTTPStatus.CREATED


class JobResource(Resource):

    def get(self, job_id):
        """GET Method to fetch job with specific ID"""
        job = Job.get_by_id(job_id=job_id)
        
        if job is None:
            return {"message": "job not found"}, HTTPStatus.NOT_FOUND
        
        if job.is_published is False:
            return {"message": "job not published"}, HTTPStatus.FORBIDDEN

        return job.data, HTTPStatus.OK
    
    def put(self, job_id):
        """PUT Method to update the specific job."""
        data = request.get_json()

        job = Job.get_by_id(job_id=job_id)

        if job is None:
            return {"message": "job not found"}, HTTPStatus.NOT_FOUND
        
        job.title = data["title"]
        job.description = data["description"]
        job.salary = data["salary"]

        # Save the update to database
        job.save()

        return job.data, HTTPStatus.OK
    
    def delete(self, job_id):
        """DELETE Method to delete specific job."""
        job = Job.get_by_id(job_id=job_id)
        
        if job is None:
            return {"message": "job not found"}, HTTPStatus.NOT_FOUND
        
        # Delete the job from the database
        job.delete()

        return {}, HTTPStatus.NO_CONTENT


class JobPublishResource(Resource):

    def put(self, job_id):
        """PUT Method to publish specific job."""
        job = Job.get_by_id(job_id=job_id)
        
        if job is None:
            return {"message": "job not found"}, HTTPStatus.NOT_FOUND
        
        job.is_published = True

        # Save the changes
        job.save()

        return {}, HTTPStatus.OK
    
    def delete(self, job_id):
        """DELETE Method to delete specific job."""
        job = Job.get_by_id(job_id=job_id)
        
        if job is None:
            return {"message": "job not found"}, HTTPStatus.NOT_FOUND
        
        job.is_published = False

        # Save the changes
        job.save()

        return {}, HTTPStatus.OK