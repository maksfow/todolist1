from database.models import Tag
from database import get_db
# Создание тегов
def careste_tag(category):
    db = next(get_db())
    new_tag = Tag(category=category)
    db.add(new_tag)
    db.commit()
    return f'Успешно создан {new_tag.category_id}'
# Получить все теги
def get_tags():
    db = next(get_db())
    tags = db.query(Tag).all()
    return tags
# Получить все задания определенного тега
async def fetch_tasks_by_category(category):
    db = next(get_db())
    checker = db.query(Tag).filter_by(category=category).all()
    if checker:
        return [task.name for task in checker]
    else:
        return 'Ничего не найдено'
# Удаление тега
async def delete_category(category_id):
    db = next(get_db())
    task = db.query(Tag).filter_by(category_id=category_id).first()
    if task:
        db.delete(task)
        db.commit()
        return f' {category_id} удален'
    else:
        return 'Тег не найден'
# Изменение тега
def edit_tag(category, edit_info, new_info):
    db = next(get_db())
    exact_tag = db.query(Tag).filter_by(category=category).first()
    if exact_tag:
        if edit_info == 'name':
           if exact_tag.name is None:
              exact_tag.name = new_info
           else:
               if new_info not in exact_tag.name:
                   exact_tag.name += ',' + new_info

        db.commit()

        return 'Задание успешно изменено!'
    else:
        return 'Задание не найдено'


