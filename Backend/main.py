from fastapi import FastAPI
from Backend.routes import auth, members
from Backend import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(members.router)
