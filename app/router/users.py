from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session


from ..database import get_db
from ..models import User
from ..schemas import UserCreate,UserLogin
from ..auth import hash_password, verify_password,create_access_token

router = APIRouter(tags=["Auth"])


@router.post("/register")
def register(user:UserCreate, db:Session = Depends(get_db)):
    db_user = User(
        username = user.username,
        password = hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)


    return {"message" : "User Created"}


@router.post("/login")
def login(user: UserLogin, db:Session = Depends(get_db)):

    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user:
        raise HTTPException(status_code=400,detail="invalid credentails")
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="invalid credentials")
    
    token = create_access_token({"user_id" : db_user.id})

    return {"access_token" : token, "token_type": "bearer"}