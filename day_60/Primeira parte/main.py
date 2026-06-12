from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    if data.get('username') and data.get('password'):
        print(data)
        return 'Welcome back, ' + data.get('username')
    else:
        return 'Please fill in all fields'


if __name__ == '__main__':
    app.run(debug=True)