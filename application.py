from flask import Flask, session, render_template

app = Flask(__name__)

# Main page
@app.route("/")
def index():
    return render_template('index.html')
