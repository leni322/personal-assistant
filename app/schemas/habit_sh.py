from pydantic import BaseModel

class HabitBase(BaseModel):
    title: str
    description: str | None = None

class HabitCreate(HabitBase):
    pass

class HabitUpdate(BaseModel):
    title: str | None = None
    description: str | None = None

class Habit(HabitBase):
    id: int

    class Config:
        orm_mode = True
