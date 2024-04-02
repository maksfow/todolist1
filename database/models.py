from sqlalchemy import Column, String, Integer,Date, DateTime,ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base
# Таблица пользователя
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String)
    surname = Column(String)
    phone_number = Column(String, unique=True)
    password = Column(String)
    city = Column(String)
    reg_date = Column(DateTime)
    tasks = Column(String, ForeignKey('tasks.title'))
    tasks_fk = relationship('Task', foreign_keys=[tasks], lazy='subquery')
# Таблица category
class Tag(Base):
    __tablename__ = 'tags'
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String)
    name = Column(String,ForeignKey('tasks.title_id'))
    name_fk = relationship('Task',foreign_keys=[name], lazy='subquery')
# Таблица задач
class Task(Base):
    __tablename__ = 'tasks'
    host_id = Column(Integer)
    title_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(Text)
    status = Column(String)
    user_id = Column(String, ForeignKey('users.user_id'))
    due_date = Column(Date)
    category = Column(String)
    user_id_fk = relationship('User',foreign_keys=[user_id],lazy='subquery')
# Таблица комм
class Comment(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(Integer, ForeignKey('users.user_id'))
    post_id = Column(Integer, ForeignKey('tasks.title_id'))
    comment_text = Column(Text)
    publish_date = Column(DateTime)
    user_fk = relationship(User,foreign_keys=[userid], lazy='subquery')
    post_fk = relationship(Task,foreign_keys=[post_id], lazy='subquery')