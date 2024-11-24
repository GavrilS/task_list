from flask import (
    Flask, render_template, url_for, request
)
from markupsafe import escape

def create_app():
    app = Flask(__name__)

    # Hidden urls -> having some fun with the users
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        # return 'Hello World!'
        return render_template('greeting/hello.html')
    
    # Escaping HTML
    @app.route('/<name>', methods=['GET', 'POST'])
    def greet_person(name):
        if request.method == 'POST':
            return f"You are doing a POST request in the greeting section, {escape(name)}"
        else:
            return f"Hello, {escape(name)}!"
    # End of HUs

    with app.test_request_context():
        print(url_for('hello'))
        print(url_for('hello', query_param='!', next='/'))
        print(url_for('greet_person', name='John Doe'))

    return app
