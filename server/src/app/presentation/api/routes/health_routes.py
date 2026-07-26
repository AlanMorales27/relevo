from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.app.core import get_data_base

router = APIRouter(tags=["health"])

@router.get("/health")
def health_check(db: Session = Depends(get_data_base)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception:
        return {"status": "error"}
