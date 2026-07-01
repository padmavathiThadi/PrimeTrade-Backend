from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Depends
from app.models import User, Login
from app.database import users, tasks
from app.task_model import Task
from app.auth import hash_password, verify_password, create_access_token, verify_token
from bson import ObjectId

app = FastAPI(title="PrimeTrade Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "PrimeTrade Backend API is running successfully!"}

@app.post("/register")
def register(user: User):
    user_data = user.model_dump()

    # Hash the password before saving
    user_data["password"] = hash_password(user.password)

    users.insert_one(user_data)

    return {
        "message": "User registered successfully"
    }
@app.post("/login")
def login(user: Login):

    db_user = users.find_one({"email": user.email})

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token(
        {
            "email": db_user["email"],
            "role": db_user.get("role", "user")
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@app.get("/dashboard")
def dashboard(user=Depends(verify_token)):
    return {
        "message": "Welcome to PrimeTrade Dashboard!",
        "user": user
    }

@app.post("/tasks")
def create_task(task: Task):
    task_data = task.model_dump()
    tasks.insert_one(task_data)

    return {
        "message": "Task created successfully"
    }
@app.get("/tasks")
def get_tasks():
    all_tasks = []

    for task in tasks.find():
        task["_id"] = str(task["_id"])
        all_tasks.append(task)

    return all_tasks
@app.put("/tasks/{task_id}")
def update_task(task_id: str, task: Task):

    tasks.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": task.model_dump()}
    )

    return {
        "message": "Task updated successfully"
    }
@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):

    tasks.delete_one({"_id": ObjectId(task_id)})

    return {
        "message": "Task deleted successfully"
    }