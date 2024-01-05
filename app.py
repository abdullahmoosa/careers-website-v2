# Module name must start with lowercase
# To render a template, we can use the "render_template" function
import json
from flask import Flask, render_template, url_for,jsonify, request
from database import load_jobs_from_db, load_job_from_db
app = Flask(__name__)

@app.route('/')
def render_jobs():
    JOBS =load_jobs_from_db()
    return render_template('home.html',jobs = JOBS)

@app.route('/api/jobs')
def list_jobs():
    JOBS =load_jobs_from_db()
    return jsonify(JOBS)

@app.route('/job/<id>')
def get_job(id):
    job = load_job_from_db(id)

    if job:
        print(f"Type of job is {type(job)}")
        return render_template('job_description.html',job = job)
    else:
        return jsonify({"error": f"Job with id = {id} not found"}), 404

@app.route('/job/<id>/apply', methods = ['post'])
def apply_to_job(id):
    data = request.form
    return render_template('application_submitted.html',application = data)

if __name__ == '__main__':
    app.run(debug=True)