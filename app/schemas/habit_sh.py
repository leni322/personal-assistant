from pydantic import BaseModel

class HabitBase(BaseModel):
    title: str
    description: str | None = None

class HabitCreate(HabitBase):
    pass

class Habit(HabitBase):
    id: int

    class Config:
        orm_mode = True
