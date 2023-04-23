from fastapi import FastAPI, HTTPException, status
from subprocess import Popen, PIPE

app = FastAPI(title="SafeBoard API")


myprocess = None


# Документация
# @app.get("/api/docs")
# async def get_docs():
#     return FastAPI().swagger_ui_html()


# Запуск процесса
@app.post("/api/{pn}/start")
async def start_process(pn: str):
    global myprocess

    if myprocess is not None and myprocess.poll() is None:
        raise HTTPException(status_code=409, detail="Process already running")

    myprocess = Popen(["python", "process.py"], stdout=PIPE)

    return {"message": "Process started"}


# Остановка процесса
@app.post("/api/{pn}/stop")
async def stop_process(pn: str):
    global myprocess

    if myprocess is None and myprocess.poll() is not None:
        raise HTTPException(status_code=404, detail="Process not found")

    myprocess.terminate()
    myprocess = None

    return {"message": "Process stopped"}


# Статус процесса
@app.get("/api/{pn}")
async def get_status(pn: str):
    global myprocess

    if myprocess is None or myprocess.poll() is not None:
        return {"status": "Process not running"}

    return {"status": "Process running"}


# Результат работы процесса
@app.get("/api/{pn}/result")
async def get_result(pn: str):
    global myprocess

    if myprocess is None or myprocess.poll() is not None:
        raise HTTPException(status_code=404, detail="Process not found")

    result = myprocess.stdout.read()

    return {"result": result.decode("utf-8")}
