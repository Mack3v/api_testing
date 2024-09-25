from pydantic import BaseModel, RootModel
from typing import List

class UserModel(BaseModel):
    id: int
    name: str
    email: str
    gender: str
    status: str

class UsersResponseModel(RootModel):
    root: List[UserModel]
