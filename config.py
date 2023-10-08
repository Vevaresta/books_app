class Config:
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://kec:root@localhost/worktastic"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False