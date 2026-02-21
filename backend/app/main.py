from fastapi import FastAPI
from app.routes import auth, reports

app = FastAPI(title="MDH Secure Financial Report API")

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(reports.router, prefix="/api/reports", tags=["Reports"])