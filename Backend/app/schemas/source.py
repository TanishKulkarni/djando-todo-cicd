from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class SourceCreate(BaseModel):
    project_id: UUID
    source_type: str
    content: str


class SourceResponse(BaseModel):
    id: UUID
    project_id: UUID
    source_type: str
    content: str
    uploaded_by: UUID | None
    created_at: datetime

    class Config:
        from_attributes = True