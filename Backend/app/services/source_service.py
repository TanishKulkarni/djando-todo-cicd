from sqlalchemy.orm import Session

from app.models.source import Source
from app.schemas.source import SourceCreate


def create_source(
    db: Session,
    source_data: SourceCreate,
    uploaded_by: int | None = None
):
    source = Source(
        project_id=source_data.project_id,
        source_type=source_data.source_type,
        content=source_data.content,
        uploaded_by=uploaded_by
    )

    db.add(source)
    db.commit()
    db.refresh(source)

    return source


def get_sources(db: Session):
    return db.query(Source).all()


def delete_source(db: Session, source_id: int):
    source = db.query(Source).filter(
        Source.id == source_id
    ).first()

    if not source:
        return None

    db.delete(source)
    db.commit()

    return source