from fastapi import FastAPI

app = FastAPI()

@app.get('/app/hello')
def hello_world():
    return {"Hello":"World"}