from flask import Flask, redirect, render_template, request


users = [
  {
    'id': 4,
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'johndoe@gmail.com',
  },
  {
    'id': 6,
    'first_name': 'John2',
    'last_name': 'Doe2',
    'email': 'john4rffdoe@gmail.com',
  },
]


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/users', methods=['GET'])
def get_users():
    return render_template('users/index.html', users=users)


@app.route('/users', methods=['POST'])
def post_user():
    if request.form['first_name']:
      if request.form['last_name']:
        users.append({'first_name': request.form['first_name'],
                      'last_name': request.form['last_name']})
        return redirect('/users', code=302)
      else:
        return "Last name can't be blank", 422
    else:
      return "First name can't be blank", 422


@app.route('/users/create' , methods=['GET'])
def get_form():
    return render_template('users/create.html')
