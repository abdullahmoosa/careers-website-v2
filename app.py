# Module name must start with lowercase
# To render a template, we can use the "render_template" function
from flask import Flask, render_template, url_for

app = Flask(__name__)

JOBS = [
    {'id' : 1,
     'title' : 'Data Analyst',
     'location' : 'Bengaluru, India',
     'Salary' : 'Rs. 10,00,000'
    },
    {'id' : 2,
     'title' : 'Data Scientist',
     'location' : 'Delhi, India',
     'Salary' : 'Rs. 15,00,000'
    },
    {'id' : 3,
     'title' : 'Frontend Developer',
     'location' : 'Remote',
     'Salary' : 'Rs. 10,00,000'
    },
    {'id' : 4,
     'title' : 'Backend Developer',
     'location' : 'San Francisco,USA',
     'Salary' : '$ 120,000'
    },
]

@app.route('/')
def hello_world():
    return render_template('home.html',jobs = JOBS)


if __name__ == '__main__':
    app.run(debug=True)