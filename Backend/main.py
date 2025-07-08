from fastapi import FastAPI
from routes import auth, members

app = FastAPI()

app.include_router(auth.router)
app.include_router(members.router)

@app.get("/")
async def root():
    return {"message": "Backend running!"}
