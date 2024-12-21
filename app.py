from task_list_app import create_app, auth

def main():
    app = create_app()

    app.register_blueprint(auth.bp)

    app.run(debug=True)



if __name__=='__main__':
    main()
