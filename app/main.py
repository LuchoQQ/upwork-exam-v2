from fastapi import FastAPI 

from .routers import users
from .routers import profiles

app = FastAPI()

app.include_router(users.router)
app.include_router(profiles.router)


