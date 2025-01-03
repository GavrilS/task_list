"""
Functionality:
- create task and save to db(if created by a registered user/admin?)
- get task/s for a user/admin?
- edit task/s for a user/admin?
- delete task/s for a user/admin?
"""
from datetime import datetime
from flask import (
    Blueprint, request, flash, redirect, url_for, render_template, session, g
)

from .db import (
    engine, create_task, get_task, get_all_user_tasks, update_task, delete_task
)

bp = Blueprint('user', __name__, '/user')

priority_mapping = {
    'Critical': 1,
    'High': 2,
    'Normal': 3,
    'Low': 4
}

@bp.route('/<user_id>/tasks', methods=('GET', 'POST', 'PUT', 'DELETE'))
def tasks(user_id=None):
    tasks = []
    error = None
    if not user_id:
        error = 'Missing user id...'
    else:
        if request.method == 'POST':
            print(request.form)
            function = request.form.get('function', '')

            if function == 'create':
                tasks = add_new_task(user_id)
            elif function == 'update':
                tasks = edit_task(user_id)
            else:
                task_id = request.form.get('task_id', None)
                if task_id:
                    tasks = remove_task(user_id, task_id)

        else:
            tasks = retrieve_user_tasks(user_id)
            
        
        return render_template('user/tasks.html', tasks=tasks)

def add_new_task(user_id):
    task_data = get_task_data()

    with engine.connect() as connection:
        create_task(connection, task_data)
        tasks = get_all_user_tasks(connection, user_id)
    
    return tasks

def edit_task(user_id):
    task_data = get_task_data()

    with engine.connect() as connection:
        update_task(connection, task_data)
        tasks = get_all_user_tasks(connection, user_id)
    
    return tasks

def remove_task(user_id, task_id):
    with engine.connect() as connection:
        delete_task(connection, task_id)
        tasks = get_all_user_tasks(connection, user_id)
    
    return tasks

def retrieve_user_tasks(user_id):
    with engine.connect() as connection:
        tasks = get_all_user_tasks(connection, user_id)
    
    return tasks

def get_task_data():
    task_id = request.form.get('id', '')
    title = request.form['title']
    description = request.form['description']
    priority = request.form['priority']
    priority_value = priority_mapping.get(priority, '4')
    task_data = {
        'id': task_id,
        'title': title,
        'description': description,
        'user_id': user_id,
        'priority': priority,
        'priority_value': priority_value
    }

    return task_data