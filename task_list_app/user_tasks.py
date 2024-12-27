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

@bp.route('/<user_id>/tasks', methods=('GET', 'POST'))
def tasks(user_id=None):
    tasks = []
    error = None
    if not user_id:
        error = 'Missing user id...'
    else:
        if request.method == 'POST':
            pass
        
        else:
            with engine.connect() as connection:
                tasks = get_all_user_tasks(connection, user_id)
            
            return render_template('user/tasks.html', tasks=tasks)
