from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    
    # return a render_template instead of a hard coded string
    data_from_database = {"user1": "user1firstname"}
    return render_template('index.html', data=data_from_database)
    
@app.route('/about')
def about(): # new view function about

    # return a render_template instead of hard coded about string
    about_data = {"owner1": "owner_firstName"}
    return render_template('about.html', owner=about_data)
    
@app.route('/helloworld/<name>')
def helloworld(name): # new view function about
    print(name)
    return_message = "Hello World {}".format(name)
    return return_message 

@app.route('/welcome/<username>')

def welcome(username):
    print(username)
    return "Welcome Dear {}".format(username)

@app.route('/contact')
def contact(): # new view function contact
    return "my email is ...@gmail.com"

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)