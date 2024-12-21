from flask import (
    Flask, render_template, url_for, request
)
from markupsafe import escape
# from . import auth

tasks = [
    {
        'title': 'Task 1',
        'description': 'Take the trash out',
        'priority_value': '3',
        'priority': 'Normal'
    },
    {
        'title': 'Task 2',
        'description': 'Feed the baby',
        'priority_value': '1',
        'priority': 'Urgent'
    },
    {
        'title': 'Task 3',
        'description': 'Take the dog for a walk and feed it afterwards',
        'priority_value': '2',
        'priority': 'High'
    }
]

tasks2 = []

def create_app():
    app = Flask(__name__)

    # app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html', tasks=tasks)
        # return render_template('index.html', tasks=tasks2)

    # Hidden urls -> having some fun with the users
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        # return 'Hello World!'
        return render_template('greeting/hello.html')
    
    # Escaping HTML
    @app.route('/hello/<name>', methods=['GET', 'POST'])
    def greet_person(name):
        if request.method == 'POST':
            return f"You are doing a POST request in the greeting section, {escape(name)}"
        else:
            # return f"Hello, {escape(name)}!"
            return render_template('greeting/hello.html', name=escape(name))
    # End of HUs

    with app.test_request_context():
        print(url_for('hello'))
        print(url_for('hello', query_param='!', next='/'))
        print(url_for('greet_person', name='John Doe'))

    return app
