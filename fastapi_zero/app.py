from fastapi import FastAPI

app = FastAPI()


# isso é o que executa a rota quando chamado /
@app.get('/')
def read_root():
    return {'message': 'Hello World'}
