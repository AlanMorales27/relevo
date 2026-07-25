from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from server.src.app.core.database import get_data_base

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check(db: Session = Depends(get_data_base)):
    try:
        db.execute("SELECT 1")
        return {"status": "ok"}
    except Exception:
        return {"status": "error"}
