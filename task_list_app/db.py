import os
from datetime import datetime
from sqlalchemy import create_engine, text


DB_USER = os.getenv('DB_USER', '')
DB_PASS = os.getenv('DB_PASS', '')
DB_SERVER = os.getenv('DB_SERVER', 'localhost')
DB_PORT = os.getenv('DB_PORT', 3306)
DB_NAME = os.getenv('DB_NAME', 'task_list')

connection_string = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"

engine = create_engine(connection_string, echo=True)


def create_user(connection, user_data):
    if not validate_user_data(user_data, 'create'):
        raise Exception('User data is missing... Cannot create a new user!')

    query = f"INSERT INTO user(name,email,password) VALUES ('{user_data['name']}','{user_data['email']}','{user_data['password']}');"
    connection.execute(text(query))
    connection.commit()

def update_user(connection, user_data):
    pass

def delete_user(connection, user_data):
    pass

def get_user(connection, user_data):
    if not validate_user_data(user_data, 'get'):
        raise Exception('User data is missing... Cannot get a user without id or email!')
    if user_data.get('id', None):
        query = f"SELECT * FROM user WHERE id = {user_data['id']} AND active = 1 AND type != 'admin';"
    else:
        query = f"SELECT * FROM user WHERE email = '{user_data['email']}' AND active = 1 AND type != 'admin';"
    
    res = connection.execute(text(query))

    user = None
    try:
        for row in res.mappings():
            user = row
    except Exception as e:
        print(f"Exception get user with query: {query}. \n {e}")
    
    return user

def get_all_users(connection):
    query = "SELECT * FROM user WHERE active = 1 AND type != 'admin';"
    res = connection.execute(text(query))
    users = []
    try:
        for row in res.mappings():
            users.append(row)
    except Exception as e:
        print(f"Exception getting all users with query: {query}. \n {e}")
    
    return users

def create_task(connection, task_data):
    if not validate_task_data(task_data, 'create'):
        raise Exception('Required task data is missing... Cannot create a new task!')
    
    query = "INSERT INTO task(title, user_id, description, priority_value, priority, created_at) " \
        f"VALUES ('{task_data['title']}','{task_data['user_id']}','{task_data.get('description', '')}',{task_data.get('priority_value', 4)},'{task_data.get('priority', 'Low')}',{task_data.get('create_at', datetime.now())});"
    connection.execute(text(query))
    connection.commit()

def get_task(connection, task_data):
    if not validate_task_data(task_data):
        raise Exception('Required task data is missing... Cannot create a new task!')
    query = f"SELECT * FROM task WHERE title = '{task_data['title']}' and user_id = {task_data['user_id']} AND active = 1"
    res = connection.execute(text(query))
    task = None
    try:
        for row in res.mappings():
            task = row
    except Exception as e:
        print(f"Error getting results from query: {query}. \n {e}")
    
    return task

def get_all_user_tasks(connection, user_id=None):
    if not user_id:
        raise('Cannot get tasks because a user id was not provided...')
    query = f"SELECT * FROM task WHERE user_id = {user_id} AND active = 1"
    res = connection.execute(text(query))
    tasks = []
    try:
        for row in res.mappings():
            tasks.append(row)
    except Exception as e:
        print(f"Error getting results from query: {query}. \n {e}")
    
    return tasks

def update_task(connection, task_data):
    pass

def delete_task(connection, task_data):
    pass

def validate_user_data(data, request_type='get'):
    if 'get' in request_type.lower():
        return data.get('id', None) or data.get('email', None)
    else:
        return data.get('name', None) and data.get('email', None) and data.get('password', None)

def validate_task_data(data):
    return  data.get('title', None) and data.get('user_id', None)
