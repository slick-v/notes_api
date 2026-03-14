from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt 
from sqlalchemy.orm import Session

from .database import get_db
from .models import *
from .auth import SECRET_KEY,ALGORITHM


oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")



def get_current_user(token:str = Depends(oauth2_scheme), db:Session = Depends(get_db)):
    
    payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])

    user_id = payload.get("user_id")
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=401, detail="Inavalid authentication")
    
    return user