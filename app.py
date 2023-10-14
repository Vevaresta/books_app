from flask import Flask
from flask_restful import Api
from resources.job import JobListResource, JobResource, JobPublishResource
from config import Config
from extensions import db, jwt
from flask_migrate import Migrate
from models.user import User
from resources.token import RefreshResource, TokenResource
from resources.user import UserListResource
import logging
import logging.config


# Initiate the app
app = Flask(__name__)

# Server logging config
logging.config.fileConfig('logging_config')

# create logger
logger = logging.getLogger("server_log")

# Configuration file
app.config.from_object(Config)

# Initialize Database
db.init_app(app)
migrate = Migrate(app, db)

# JWT Token
jwt.init_app(app)

# Flask Restful
api = Api(app)

# Routing
api.add_resource(JobListResource, "/jobs")
api.add_resource(JobResource, "/jobs/<int:job_id>")
api.add_resource(JobPublishResource, "/jobs/<int:job_id>/publish")

api.add_resource(UserListResource, "/users")

api.add_resource(TokenResource, "/token")
api.add_resource(RefreshResource, "/refresh")

# Start server
if __name__ == "__main__":
    app.run(port=5000, debug=True)