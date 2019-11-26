from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	user = {'username' : 'Steve'}
	posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
	return render_template('index.html', title='Home', user=user, posts=posts)

if __name__ == '__main__':
	app.run()
