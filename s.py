from fastapi import FastAPI
import uvicorn
app = FastAPI()
@app.get('/')
def home():
    return 'api is active'

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000) 