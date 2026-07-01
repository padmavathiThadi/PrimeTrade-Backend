from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str
    role: str = "user"


class Login(BaseModel):
    email: str
    password: str