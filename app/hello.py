from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	user = {'username' : 'Steve'}
	name = request.args.get("name", "World")
	return render_template('index.html', title='Home', user=user)

if __name__ == '__main__':
	app.run()
