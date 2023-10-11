class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///worktastic.db'   
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "my-secret-key"
    JWT_ERROR_MESSAGE_KEY = "message"