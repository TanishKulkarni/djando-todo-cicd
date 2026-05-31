from app.models.project import Project

from app.repositories.project_repository import (
    create_project,
    get_projects_by_user,
    get_project_by_id,
    update_project,
    delete_project
)


def create_new_project(
    db,
    user_id,
    name,
    description
):
    project = Project(
        user_id=user_id,
        name=name,
        description=description
    )

    return create_project(
        db,
        project
    )


def get_all_projects(
    db,
    user_id
):
    return get_projects_by_user(
        db,
        user_id
    )


def get_single_project(
    db,
    project_id,
    user_id
):
    project = get_project_by_id(
        db,
        project_id
    )

    if not project:
        return None

    if str(project.user_id) != str(user_id):
        return None

    return project


def update_existing_project(
    db,
    project_id,
    user_id,
    name,
    description
):
    project = get_single_project(
        db,
        project_id,
        user_id
    )

    if not project:
        return None

    project.name = name
    project.description = description

    return update_project(
        db,
        project
    )


def remove_project(
    db,
    project_id,
    user_id
):
    project = get_single_project(
        db,
        project_id,
        user_id
    )

    if not project:
        return False

    delete_project(
        db,
        project
    )

    return True