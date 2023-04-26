from fastapi import FastAPI
import uvicorn
app = FastAPI()
@app.get('/')
def home():
    return 'api is active '
