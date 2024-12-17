import os
from datetime import datetime
from sqlalchemy import create_engine, text


DB_USER = os.getenv('DB_USER', '')
DB_PASS = os.getenv('DB_PASS', '')
DB_SERVER = os.getenv('DB_SERVER', '')
DB_PORT = os.getenv('DB_PORT', '')
DB_NAME = os.getenv('DB_NAME', 'task_list')

connection_string = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"

engine = create_engine(connection_string, echo=True)


def create_user(connection, user_data):
    if not validate_user_data(user_data):
        raise Exception('User data is missing... Cannot create a new user!')

    query = f"INSERT INTO user(name,email,password) VALUES ({user_data['name']},{user_data['email']},{user_data['password']})"
    connection.execute(text(query))
    connection.commit()

def get_user(conenction, user_data):
    pass

def create_task(connection, task_data):
    if not validate_task_data(task_data):
        raise Exception('Required task data is missing... Cannot create a new task!')
    
    query = "INSERT INTO task(title, user_id, description, priority_value, priority, created_at) " \
        f"VALUES ({task_data['title']},{task_data['user_id']},{task_data.get('description', '')},{task_data.get('priority_value', 4)},{task_data.get('priority', 'Low')},{task_data.get('create_at', datetime.now())})"
    connection.execute(text(query))
    connection.commit()

def get_task(conenction, task_data):
    pass

def validate_user_data(data):
    return data.get('name', None) and data.get('email', None) and data.get('password', None)

def validate_task_data(data):
    return  data.get('title', None) and data.get('user_id', None)
