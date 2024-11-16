from flask import (
    Flask, render_template, url_for
)

def create_app():
    app = Flask(__name__)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        # return 'Hello World!'
        return render_template('greeting/hello.html')

    return app
