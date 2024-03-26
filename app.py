from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Kevin Sieber! I am adding my first code change!'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')


@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():  # put application's code here
    return render_template('about-css.html')

@app.route('/favorite-course')
def favoritecourse():
    return render_template('favorite-course.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()
