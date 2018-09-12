from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return 'Blog App'
    
@app.route('/index')
def index():
    users = ['user1', 'user2']
    articles = ['article1', 'article2']
    return render_template('index.html', articles=articles,users=users)
    
if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)