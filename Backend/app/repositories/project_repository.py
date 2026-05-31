from sqlalchemy.orm import Session

from app.models.project import Project


def create_project(
    db: Session,
    project: Project
):
    db.add(project)
    db.commit()
    db.refresh(project)

    return project


def get_projects_by_user(
    db: Session,
    user_id
):
    return (
        db.query(Project)
        .filter(Project.user_id == user_id)
        .order_by(Project.created_at.desc())
        .all()
    )


def get_project_by_id(
    db: Session,
    project_id
):
    return (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )


def update_project(
    db: Session,
    project
):
    db.commit()
    db.refresh(project)

    return project


def delete_project(
    db: Session,
    project
):
    db.delete(project)
    db.commit()