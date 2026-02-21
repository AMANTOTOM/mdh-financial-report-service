from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import decode_token
from app.services.report_service import generate_report

router = APIRouter()
security = HTTPBearer()

def authorize(credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = decode_token(credentials.credentials)
    if payload["role"] != "MDH_MANAGER":
        raise HTTPException(status_code=403, detail="Forbidden")
    return payload


@router.get("/financial")
def get_financialgi_report(creator: str = None, platform: str = None, user=Depends(authorize)):
    return generate_report(creator, platform)