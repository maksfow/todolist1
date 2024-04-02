from fastapi import FastAPI
from users.user_api import user_router
from comment_api.comments import comment_router
from tag_api.tags import tag_router
from task_api.tasks import task_router
from database import Base, engine
Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url='/')
app.include_router(user_router)
app.include_router(comment_router)
app.include_router(tag_router)
app.include_router(task_router)