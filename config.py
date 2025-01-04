import os 
# configuration file allows us to perform seprartion of concerns. 
# the class stores the configuration variables 

class Config: 
    SECRET_KEY = os.environ.get("SECRET KEY") or "you will never guess"