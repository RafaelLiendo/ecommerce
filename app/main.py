from fastapi import FastAPI, Depends
from starlette.requests import Request
import uvicorn

from app.api.admin.routers.users import users_router
from app.api.admin.routers.auth import auth_router
from app.core import config
from app.db.session import SessionLocal
from app.core.auth import get_current_active_user
from app.core.celery_app import celery_app
from app import tasks


app = FastAPI(title=config.PROJECT_NAME, docs_url="/")

auth = FastAPI(title=config.PROJECT_NAME + " auth", docs_url="/")

admin = FastAPI(title=config.PROJECT_NAME + " admin", docs_url="/")

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response

# Routers
app.include_router(
    users_router,
    tags=["users"],
    dependencies=[Depends(get_current_active_user)],
)
auth.include_router(auth_router, tags=["auth"])

app.mount('/auth', auth);

admin.include_router(users_router, tags=["users"])

app.mount('/admin', admin)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
