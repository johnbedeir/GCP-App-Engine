from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a Flask app running on Google App Engine in Germany.'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
