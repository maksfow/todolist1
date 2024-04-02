from database.models import Task
from database import get_db
# Добавление задания
async def add_new_task(host_id, title, description, status, due_date, category):
    db = next(get_db())
    new_task = Task(host_id=host_id, title=title, description=description, status=status, due_date=due_date,
                    category=category)
    db.add(new_task)
    db.commit()
    return new_task.title_id
# Получить все задания
async def get_tasks():
    db = next(get_db())
    tasks = db.query(Task).all()
    return tasks
# Получить определенные задания
async def get_exact_task(category):
    db = next(get_db())
    tasks = db.query(Task).filter_by(category=category).all()
    if tasks:
        task_titles = [task.title for task in tasks]
        return ', '.join(task_titles)
    else:
        return 'Ничего не найдено'


#  Удаление задания
def delete_task(title_id):
    db = next(get_db())
    task = db.query(Task).filter_by(title_id=title_id).first()
    if task:
        db.delete(task)
        db.commit()
        return f' {title_id} удален'
    else:
        return 'Задание не найдено'
# Изменения задания
def edit_task(title_id, edit_info, new_info):
    db = next(get_db())
    exact_task = db.query(Task).filter_by(title_id=title_id).first()

    if exact_task:
        if edit_info == 'description':
            exact_task.description = new_info
        elif edit_info == 'title':
            exact_task.title = new_info
        elif edit_info == 'due_date':
            exact_task.due_date = new_info
        elif edit_info == 'category':
            exact_task.category = new_info
        if edit_info == 'user_id':
            if exact_task.user_id is None:
                exact_task.user_id = new_info
            else:
                if new_info not in exact_task.user_id:
                    exact_task.user_id += ',' + new_info
        db.commit()
        return 'Задание успешно изменено!'
    else:
        return 'Задание не найдено'

async def get_exact_users(title):
    db = next(get_db())
    checker = db.query(Task).filter_by(title=title).all()
    if checker:
        users_id = [str(users.user_id) for users in checker if users.user_id is not None]
        return ', '.join(users_id)
    else:
        return 'Ничего не найдено'

