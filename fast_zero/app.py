from fastapi import FastAPI

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello World'}


@app.get('/hello_world')
def hello_world() -> Message:
    return Message(message='Hello World')
