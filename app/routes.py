# routes handle the different urls that the app supports 
# handles for the app routes are writen as python funcs - called View Functions
# View functions are mapped to one or > URLS so flask knows what logic 
# to execture whena cleint requests a given URL. 

# The view function here just returns a greeting for these two urls
from flask import render_template
from app import app 


# decorators here will be modify the function of index()
# this will be to register a function as a callback for a certain event 
# the app.route decorator creates an association between the url given 
# as an argument for the function index() below. 
# so when the browser requests / or index urls flask will invoke this function 
# and pass its return value back to the browser as a response. 

# Templates will be used in place of presentation of the html 
# allowing us to focus solely on the python code.

@app.route("/") 
@app.route("/index")
def index(): 
    user = {'username': 'Random User 1'}

    # mock example to show users information looping: 
    posts = [
        {'author': {'username':'John'}, 
         'body': 'Beautiful day in London'}, 
        {'author': {'username': 'Jane'}, 
         'body': "Weather is really nice too"},
        {'author': {'username':'Bobby'}, 
         'body': 'get outta here'}, 
        {'author': {'username': 'james'}, 
         'body': "new york is way better"}
    ]


    return render_template('index.html', title = '', user = user, posts = posts)