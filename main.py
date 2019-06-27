import flask


from flask import Flask, render_template


application = Flask(__name__)


@application.route('/')
def my_function():
    return render_template("home.html")

if __name__ == '__main__':
    application.run()