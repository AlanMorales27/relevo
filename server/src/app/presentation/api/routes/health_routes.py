import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.app.core import get_data_base

router = APIRouter(tags=["health"])

@router.get("/health")
def health_check(db: Session = Depends(get_data_base)):
    """
    Health check endpoint to verify database connectivity.
    """
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as error:
        logging.error("Health check failed: %s", error)
        raise HTTPException(status_code=503, detail="Database unavailable")
