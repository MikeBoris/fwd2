from flask import Flask, request
app = Flask(__name__)

@app.route('/<name>')
def index(name):
	return '<h1>Hello {}</h1>'.format(name)

@app.route('/')
def index1():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is {}</p>'.format(user_agent)

if __name__ == '__main__':
	app.run(debug=True)