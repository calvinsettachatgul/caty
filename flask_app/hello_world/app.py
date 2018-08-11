from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"
    
@app.route('/about')
def about(): # new view function about
    return "about page"
    
@app.route('/helloworld/<name>')
def helloworld(name): # new view function about
    print(name)
    return "hello world"

@app.route('/welcome/<username>')
def welcome(username):
    print(username)
    return "welcome"

@app.route('/contact')
def contact(): # new view function contact
    return "my email is ...@gmail.com"

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)