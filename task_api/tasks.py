from fastapi import APIRouter
from datetime import date

from database.taskservice import get_tasks, add_new_task,get_exact_users,get_exact_task,edit_task,delete_task
task_router = APIRouter(prefix='/task', tags=['Работа с заданиями'])
# Получить все задания
@task_router.get('/all-tasks')
async def all_tasks():
    return await get_tasks()
# Для добавления задания
@task_router.post('/add-task')
async def add_task(host_id: int, title: str, description: str, status: str, due_date: date, category: str):
    new_task_id = await add_new_task(host_id, title, description, status, due_date, category)
    return f'Успешно добавлен {new_task_id}'
# Получить пользователей кто выполнил определенное задание
@task_router.get('/task-users')
async def get_user_tasks(title: str):
    t_u = await get_exact_users(title)
    return f'Успешно и вот данные {t_u}'
# Изменение определенного задания
@task_router.put('/edit')
async def edit_post(title_id:int,edit_info:str, new_info:str):
    result = edit_task(title_id,edit_info, new_info)
    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка при изменении!'}
# Получить определенное задание
@task_router.get('/get-task')
async def get_task(category: str):
    result = await get_exact_task(category)
    if result:
        return {'message': result}
    else:
        return {'message': 'Такое задание отсутствует!'}
# Запрос на удаление задания
@task_router.delete('/delete_task')
async def delete_post(title_id: int):
    result = delete_task(title_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'Такое задание отсутствует'}

