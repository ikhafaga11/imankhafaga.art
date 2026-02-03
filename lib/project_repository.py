from lib.project import Project
from lib.database_connection import DatabaseConnection
from lib.project_image import ProjectImage


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
            "SELECT * FROM projects WHERE id = %s RETURNING *;", [id]
        )
        row = rows[0]
        return Project(row["title"], row["cover_image_url"], row["id"])

    def get_all_projects(self) -> list[Project]:
        rows: list[dict] = self._connection.execute("SELECT * FROM projects")
        projects_list: list[Project] = []
        for row in rows:
            projects_list.append(Project(row["title"], row["cover_image_url"], row["id"]))
        return projects_list

    def delete_project(self, id: int) -> str:
        rows: list[dict] = self._connection.execute(
            "DELETE FROM projects WHERE id = %s RETURNING: id;",
            [
                id,
            ],
        )
        deleted_row_id = rows[0]["id"]
        return f"project {deleted_row_id} deleted"

    def update_cover_image_url(self, id: int, url: str) -> Project:
        rows: list[dict] = self._connection.execute(
            "UPDATE project SET cover_image_url = %s WHERE id = %s RETURNING *",
            [
                url,
                id,
            ],
        )
        row = rows[0]
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
        row = rows[0]
        return Project(
            title=row["title"], cover_image_url=row["cover_image_url"], id=row["id"]
        )

    def post_image(self, project_image: ProjectImage) -> ProjectImage:
        rows: list[dict] = self._connection.execute(
            "INSERT INTO project_images (caption, image_url, project_id) VALUES( %s %s %s) RETURNING id;",
            [
                project_image.caption,
                project_image.image_url,
                project_image.project_id,
            ],
        )
        project_image.id = rows[0]["id"]

        return project_image

    def get_poject_image(self, id: int) -> ProjectImage:
        rows: list[dict] = self._connection.execute(
            "SELECT * FROM project_images WHERE id = %s RETURNING *; ",
            [
                id,
            ],
        )
        row:list = rows[0]
        return ProjectImage(
            caption=row["caption"],
            image_url=row["image_url"],
            id=row["id"],
            project_id=row["project_id"],
        )
    def get_all_project_images(self) -> list[Project]:
        rows: list[dict] = self._connection.execute("SELECT * FROM project_images RETURNING *;")
        project_images_list: list = []
        for row in rows:
            project_images_list.append(ProjectImage(caption=row["id"], image_url=row["image_url"], id=row["id"], project_id=row["project_id"]))
        return project_images_list

