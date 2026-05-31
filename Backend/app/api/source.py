from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.schemas.source import (
    SourceCreate,
    SourceResponse
)
from app.services.source_service import (
    create_source,
    get_sources,
    delete_source
)

router = APIRouter(
    prefix="/sources",
    tags=["Sources"]
)


@router.post(
    "",
    response_model=SourceResponse
)
def create_source_api(
    payload: SourceCreate,
    db: Session = Depends(get_db)
):
    return create_source(db, payload)


@router.get(
    "",
    response_model=list[SourceResponse]
)
def get_sources_api(
    db: Session = Depends(get_db)
):
    return get_sources(db)


@router.delete("/{source_id}")
def delete_source_api(
    source_id: UUID,
    db: Session = Depends(get_db)
):
    deleted = delete_source(
        db,
        source_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Source not found"
        )

    return {
        "message": "Source deleted successfully"
    }