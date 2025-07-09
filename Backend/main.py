from fastapi import FastAPI
from Backend.routes import auth, members
from Backend import models, database

#tio
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


import os

# Create tables
models.Base.metadata.create_all(bind=database.engine)

# Create FastAPI app
app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return HTMLResponse(content="""
    <html>
        <head>
            <title>PipStop API</title>
            <style>
                body {
                    background-image: url('/assets/image.png');
                    background-size: cover;
                    background-position: center;
                    color: white;
                    text-align: center;
                    font-family: Arial, sans-serif;
                    padding-top: 20%;
                    margin: 0;
                }
                img {
                    width: 150px;
                    margin-bottom: 20px;
                }
            </style>
        </head>
        <body>
            <img src="/assets/logo.png" alt="PipStop Logo">
            <h1>Welcome to the PipStop API 🚀</h1>
            <p>API is running successfully</p>
        </body>
    </html>
    """, status_code=200)


# Include routers
app.include_router(auth.router)
app.include_router(members.router)

# This part is important for local runs only
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Azure provides PORT env variable
    uvicorn.run("Backend.main:app", host="0.0.0.0", port=port, reload=True)
