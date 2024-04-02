from fastapi import APIRouter

from database.tagservice import get_tags, careste_tag,delete_category,fetch_tasks_by_category,edit_tag
tag_router = APIRouter(prefix='/tag', tags=['Работа с тегами'])
# Получить все теги
@tag_router.get('/all-tags')
async def all_tags():
    return get_tags()
# Для добавления тега
@tag_router.post('/add-tag')
async def add_tag(category:str):
    new_c = careste_tag(category)
    return f'Успешно добавлен {new_c}'
# Запрос на удаление тега
@tag_router.delete('/delete_tag')
async def delete_categoryyy(category_id:int):
    result = await delete_category(category_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'Ничего не найдено'}
# Получить все задания определенного тега
@tag_router.get('/all-tasks-tag')
async def get_exact_task(category:str):
    tasks = await fetch_tasks_by_category(category)
    return tasks
# Изменение определенного тега
@tag_router.put('/edit')
async def edit_tagg(category:str,edit_info:str, new_info:str):
    result = edit_tag(category,edit_info, new_info)
    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка при изменении!'}