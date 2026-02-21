from fastapi import APIRouter, HTTPException
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter()

fake_user = {
    "username": "manager",
    "password": hash_password("password123"),
    "role": "MDH_MANAGER"
}


@router.post("/login")
def login(username: str, password: str):
    if username != fake_user["username"]:
        raise HTTPException(status_code=400, detail="User not found")

    if not verify_password(password, fake_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")




    token = create_access_token({"sub": username, "role": fake_user["role"]})
    return {"access_token": token}