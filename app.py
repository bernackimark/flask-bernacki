from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Python Developer',
    'location': 'Bengaluru, India',
    'salary': '100,000',
    'currency': 'INR'
  },
  {
    'id': 2,
    'title': 'Java Developer',
    'location': 'San Francisco, CA',
    'salary': '174,999',
    'currency': 'USD'
  },
]

@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Bernacki Tech')

@app.route('/api/jobs')
def get_all_jobs():
  return JOBS

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
