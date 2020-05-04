from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"masdessage": "Hello Worlasdasdasdasdadasdasdasdasdasdd lol anal"}