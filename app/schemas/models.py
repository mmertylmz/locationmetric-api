from pydantic import BaseModel
from typing import List, Optional

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

class ItemInDB(Item):
    hashed_password: str

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

class UserInDB(User):
    hashed_password: str

class Message(BaseModel):
    message: str

class ErrorResponse(BaseModel):
    detail: str

class SuccessResponse(BaseModel):
    success: bool
    data: Optional[dict] = None
    message: Optional[str] = None