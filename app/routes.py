from flask import (
    Flask,
    request
)
from app.database import task

app = Flask(__name__)

# REST - Representational State Transfer - Architectural design pattern for
# building network connected services.

@app.get("/")
@app.get("/tasks")
def scan():
    out = {
        "tasks": task.scan(),
        "ok": True
    }
    return out                  # by default, Flask will return a status code of 200

@app.get("/tasks/<int:pk>/")
def get_single_task(pk):
    single_task = task.select_by_id(pk)
    out = {
        "ok": True
    }
    if not single_task:
        out["ok"] = False
        out["message"] = "Task not found"
        return out, 404
    out["task"] = single_task
    return out

@app.put("/tasks/<int:pk>/")
def update(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "", 204              # 204 is no content (successful, but there's nothing to return)

@app.delete("/tasks/<int:pk>/")
def delete_task(pk):
    task.delete_by_id(pk)
    return "", 204

@app.post("/tasks")
def create_task():
    task_data = request.json
    task.insert(task_data)
    return "", 204