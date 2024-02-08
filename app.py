from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'oli'

app.run(debug=True)
