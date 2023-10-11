from flask import Flask
from flask_restful import Api
from resources.job import JobListResource, JobResource, JobPublishResource
from config import Config
from extensions import db
from flask_migrate import Migrate
from models.user import User
from resources.user import UserListResource


# Initiate the app
app = Flask(__name__)

# Configuration file
app.config.from_object(Config)

# Initialize Databank
db.init_app(app)
migrate = Migrate(app, db)

# Flask Restfull
api = Api(app)


api.add_resource(JobListResource, "/jobs")
api.add_resource(JobResource, "/jobs/<int:job_id>")
api.add_resource(JobPublishResource, "/jobs/<int:job_id>/publish")

api.add_resource(UserListResource, "/users")


if __name__ == "__main__":
    app.run(port=5000, debug=True)