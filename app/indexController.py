from flask import Flask, render_template
from flask import send_file

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/downloadResume/',  methods=['GET'])
def get_resume():
    path = "tmp/gkalikapersaud_resume.pdf"
    return send_file(path, as_attachment=True)
