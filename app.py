# Module name must start with lowercase
# To render a template, we can use the "render_template" function
from flask import Flask, render_template, url_for,jsonify
from database import load_jobs_from_db
app = Flask(__name__)

JOBS =load_jobs_from_db()
@app.route('/')
def hello_world():
    return render_template('home.html',jobs = JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(debug=True)