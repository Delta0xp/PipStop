from fastapi import FastAPI

app = FastAPI()

@app.get("/api/TEST")
async def read_root():
    
    return{"message":" piel"}
