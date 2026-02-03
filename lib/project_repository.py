from lib.project import Project
from lib.database_connection import DatabaseConnection


class ProjectRepository:
    def __init__(self, db_connection: DatabaseConnection):
        self._connection = db_connection

    def post_project(self, project: Project) -> Project:
        if project.id is not None:
            raise ValueError("Project already has an id")

        rows: list[dict] = self._connection.execute(
            "INSERT INTO projects (title, cover_image_url) VALUES (%s, %s) RETURNING id;",
            [
                project.title,
                project.cover_image_url,
            ],
        )
        project.id = rows[0]["id"]
        return project

    def get_project(self, id: int) -> Project:
        rows: list[dict] = self._connection.execute(
            "SELECT * FROM projects WHERE id = %s;", [id]
        )
        row: dict = rows[0]
        return Project(row["title"], row["cover_image_url"], row["id"])

    def get_all_projects(self) -> list[Project]:
        rows: list[dict] = self._connection.execute("SELECT * FROM projects")
        projects_list: list[Project] = []
        for row in rows:
            projects_list.append(
                Project(row["title"], row["cover_image_url"], row["id"])
            )
        return projects_list

    def delete_project(self, id: int) -> None:
        self._connection.execute(
            "DELETE FROM projects WHERE id = %s",
            [
                id,
            ],
        )

    def update_cover_image_url(self, id: int, url: str) -> Project:
        rows: list[dict] = self._connection.execute(
            "UPDATE project SET cover_image_url = %s WHERE id = %s RETURNING *",
            [
                url,
                id,
            ],
        )
        row: dict = rows[0]
        return Project(
            title=row["title"], cover_image_url=row["cover_image_url"], id=row["id"]
        )

    def update_title(self, id: int, title: str) -> Project:
        rows: list[dict] = self._connection.execute(
            "UPDATE project SET title = %s WHERE id = %s RETURNING *",
            [
                title,
                id,
            ],
        )
        row: dict = rows[0]
        return Project(
            title=row["title"], cover_image_url=row["cover_image_url"], id=row["id"]
        )
