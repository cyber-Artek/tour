import datetime


from config import app, templates
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends, Form

from sqlalchemy.orm import Session

from db import get_db, Tour



# дані якого типу ми передаємо, бо серевер вважає що всі дані ми повертаємо у форматі json


@app.get('/', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    tours = db.query(Tour).all()
    return templates.TemplateResponse('index.html', {'tours': tours, 'request': request})
    # сервер  повертає значення у форматі json


@app.post('/create-tour')
def create_tour(name: str = Form(), city: str = Form(), days: int = Form(), price: int = Form(), date: str = Form(), db:Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    date = datetime.datetime.strptime(date, '%Y-%m-%d', )
    tour = Tour(name=name, city=city, days=days, price=price, date=date)
    db.add(tour)
    db.commit()
    db.refresh(tour)
    return {'id': 'tour.id'}


@app.post("/register/")
async def register_user(username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    # Перевірка чи вже існує користувач з таким email
    if any(user["email"] == email for user in registered_users):
        raise HTTPException(status_code=400, detail="Email вже зареєстрований.")
    user = {"username": username, "email": email, "password": password}  # Пароль у реальному додатку треба хешувати!
    registered_users.append(user)
    return JSONResponse(content={"message": "Реєстрація успішна!", "user": user})



