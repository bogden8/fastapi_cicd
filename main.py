from fastapi import FastAPI
import platform
import socket
import time


app = FastAPI()
START_TIME=time.time()

@app.get("/")
def root():
    return {"status": "ok", "version": "1.0.0"}

@app.get("/health")
def health():
    uptime = round(time.time() - START_TIME, 2)
    return {"status": "healthy", "uptime_seconds": uptime}

@app.get("/info")
def info():
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.version(),
        "python_version": platform.python_version(),
    }