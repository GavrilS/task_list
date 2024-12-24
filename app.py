import uuid
from task_list_app import create_app, auth

def main():
    app = create_app()

    app.register_blueprint(auth.bp)

    secret_uuid = uuid.uuid4()
    app.secret_key = secret_uuid

    app.run(debug=True)



if __name__=='__main__':
    main()
