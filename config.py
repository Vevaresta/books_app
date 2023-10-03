class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://localhost:postgres@localhost/worktastic"
    SQLALCHEMY_TRACK_MODIFICATIONS = False