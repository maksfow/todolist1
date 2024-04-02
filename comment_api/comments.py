from fastapi import APIRouter

from database.commentservice import add_comment_db,get_task_comments_db,delete_comment_db,change_comment_db
comment_router = APIRouter(prefix='/comment', tags=['Работа с комментариями'])
# Получить все комментарии определенного задания
@comment_router.get('/all-comments')
async def all_comments(post_id:int):
    return get_task_comments_db(post_id)
# Для добавления комментария
@comment_router.post('/add-comment')
async def add_comment(post_id:int, comment_text:str, userid:int):
    new_c = add_comment_db(post_id, comment_text, userid)
    return f'Успешно добавлен {new_c}'
# Изменение определенного комментария
@comment_router.put('/edit-comment')
async def edit_comment(post_id:int, comment_id:int, new_info:str,edit_info:str):
    result = change_comment_db(post_id, comment_id, new_info,edit_info)
    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка при изменении!'}
# Запрос на удаление комментария
@comment_router.delete('/delete_comment')
async def delete_post(post_id:int, comment_id:int):
    result = delete_comment_db(post_id, comment_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'Ничего не найдено'}

