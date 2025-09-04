from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, db, models
from app.models import Habit, Base
from app.db import SessionLocal, engine

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        yield db
    finally:
        db.close()


@router.post("/habits/", response_model=schemas.Habit)
def create_habit(habit: schemas.HabitCreate, db: Session = Depends(get_db)):
    db_habit = models.habit.Habit(title=habit.title, description=habit.description)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit

@router.get("/habits/", response_model=list[schemas.Habit])
def get_habits(db: Session = Depends(get_db)):
    return db.query(models.habit.Habit).all()



@router.get("/habits")
def get_habits():
    return [{"id": 1, "title": "Зарядка"}, {"id": 2, "title": "Чтение"}, {"id": 3, "title": "Программирование"}]
