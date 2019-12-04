from flask import Flask, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'df639a184af1cc1641d48f5cc3c8482e'

posts = [
    {
        'author': 'Maciej Zawistowski',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Mythyndian',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 20, 2018'
    },
]


@app.route('/')
@app.route('/home')  # home page
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')  # home page
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'succes')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
