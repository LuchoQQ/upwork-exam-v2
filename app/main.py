## imports
from fastapi import FastAPI, responses
from .routers import users
from .routers import profiles

app = FastAPI()

## routing
app.include_router(users.router)
app.include_router(profiles.router)


## redirect root to docs
@app.get("/")
async def Redirect_To_Docs():
    return responses.RedirectResponse("/docs")