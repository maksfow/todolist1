from database.models import Comment
from datetime import datetime
from database import get_db
# Опубликовать комментарий
def add_comment_db(post_id,comment_text, userid):
    db = next(get_db())
    new_comment = Comment(post_id=post_id,comment_text=comment_text, userid=userid,
                              publish_date=datetime.now())
    if new_comment:
        db.add(new_comment)
        db.commit()
        return f'Успешно создан {new_comment.comment_id}'
    else:
        return 'Нету такого поста (('

# Удаления комментарий
def delete_comment_db(post_id, comment_id):
    db = next(get_db())
    exact_comment = db.query(Comment).filter_by(post_id=post_id, comment_id=comment_id).first()
    if exact_comment:
        db.delete(exact_comment)
        db.commit()
        return 'Успешно удален'
    else:
        return 'Ошибка'
# Изменить определенный комм
def change_comment_db(post_id, comment_id, new_info,edit_info):
    db = next(get_db())
    exact_task = db.query(Comment).filter_by(post_id=post_id,comment_id=comment_id).first()
    if exact_task:
        if edit_info == 'comment_text':
            exact_task.title = new_info
        db.commit()
        return 'Комментарий успешно изменен!'
    else:
        return 'Не найдено'
# Получить все комменты определенного задания
def get_task_comments_db(post_id):
    db = next(get_db())
    post_comments = db.query(Comment).filter_by(post_id=post_id).all()
    if post_comments:
        return post_comments
    else:
        return 'На данный момент комментарии отсутствуют'