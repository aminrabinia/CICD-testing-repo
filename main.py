import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def root():
    return {"message": "program runs successfully!!!"}

@app.get('/testmsg')
def root():
    return {"message": "welcome to test!!!"}


if __name__ == "__main__":
	uvicorn.run(app, host='0.0.0.0', port=8080)