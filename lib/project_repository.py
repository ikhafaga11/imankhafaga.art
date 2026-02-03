from lib.project import Project


class ProjectRepository:
    def __init__(self, db_connection):
        self._connection = db_connection

    def add_project(self, project: Project) -> Project:
        if project.id is not None:
            raise ValueError("Project already has an id")

        rows = self._connection.execute(
            "INSERT INTO projects (title, cover_image_url) VALUES (%s, %s) RETURNING id;",
            [
                project.title,
                project.cover_image_url,
            ],
        )

        project.id = rows[0]["id"]

        return project
