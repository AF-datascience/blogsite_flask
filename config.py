import os 
# configuration file allows us to perform seprartion of concerns. 
# the class stores the configuration variables 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config: 
    SECRET_KEY = os.environ.get("SECRET KEY") or "you will never guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
# the above is the location of the applications database