from flask import Flask
from flask_restful import Api
from resources.job import JobListResource, JobResource


# Initiate the app
app = Flask(__name__)

# Flask Restfull
api = Api(app)


api.add_resource(JobListResource, "/jobs")
api.add_resource(JobResource, "/jobs/<int:job_id>")


if __name__ == "__main__":
    app.run(port=5000, debug=True)