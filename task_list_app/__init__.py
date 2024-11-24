from flask import (
    Flask, render_template, url_for
)
from markupsafe import escape

def create_app():
    app = Flask(__name__)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        # return 'Hello World!'
        return render_template('greeting/hello.html')
    
    # Escaping HTML
    @app.route('/<name>')
    def greet_person(name):
        return f"Hello, {escape(name)}"

    return app
