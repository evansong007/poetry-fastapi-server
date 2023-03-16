import uvicorn


def start():
    uvicorn.run("poetry_demo.carsharing:app", reload=True)
