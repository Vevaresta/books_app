from flask import Flask
from flask_restful import Api
from resources.job import JobListResource, JobResource, JobPublishResource


# Initiate the app
app = Flask(__name__)

# Flask Restfull
api = Api(app)


api.add_resource(JobListResource, "/jobs")
api.add_resource(JobResource, "/jobs/<int:job_id>")
api.add_resource(JobPublishResource, "/jobs/<int:job_id>/publish")


if __name__ == "__main__":
    app.run(port=5000, debug=True)