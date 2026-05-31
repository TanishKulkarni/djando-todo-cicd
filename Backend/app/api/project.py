from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.project import (
    ProjectCreate,
    ProjectUpdate
)

from app.services.project_service import *

from app.core.dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("/")
def create_project_endpoint(
    request: ProjectCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_new_project(
        db,
        current_user.id,
        request.name,
        request.description
    )


@router.get("/")
def get_projects_endpoint(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_all_projects(
        db,
        current_user.id
    )


@router.get("/{project_id}")
def get_project_endpoint(
    project_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    project = get_single_project(
        db,
        project_id,
        current_user.id
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project


@router.put("/{project_id}")
def update_project_endpoint(
    project_id: str,
    request: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    project = update_existing_project(
        db,
        project_id,
        current_user.id,
        request.name,
        request.description
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project


@router.delete("/{project_id}")
def delete_project_endpoint(
    project_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    success = remove_project(
        db,
        project_id,
        current_user.id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {
        "message": "Project deleted successfully"
    }