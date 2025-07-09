from fastapi import FastAPI
from Backend.routes import auth, members
from Backend import models, database

import os

# Create tables
models.Base.metadata.create_all(bind=database.engine)

# Create FastAPI app
app = FastAPI()

# Include routers
app.include_router(auth.router)
app.include_router(members.router)

# This part is important for local runs only
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Azure provides PORT env variable
    uvicorn.run("Backend.main:app", host="0.0.0.0", port=port, reload=True)
