from lib.project_content import ProjectContent
from lib.database_connection import DatabaseConnection


class ProjectContentRepository:
    def __init__(self, db_connection: DatabaseConnection):
        self._connection = db_connection

    def post_content(self, content: ProjectContent) -> ProjectContent:
        rows: list[dict] = self._connection.execute(
            "INSERT INTO project_contents (caption, image_url, project_id) VALUES( %s, %s, %s) RETURNING id;",
            [
                content.caption,
                content.image_url,
                content.project_id,
            ],
        )
        content.id = rows[0]["id"]

        return content

    def delete_content(self, id: int) -> None:
        self._connection.execute(
            "DELETE FROM project_contents WHERE id = %s",
            [
                id,
            ],
        )

    def update_content(self, new_content: ProjectContent) -> ProjectContent:
        rows: list[dict] = self._connection.execute(
            "UPDATE project_contents SET caption = %s, image_url = %s WHERE id = %s RETURNING *",
            [
                new_content.caption,
                new_content.image_url,
                new_content.id,
            ],
        )
        row: dict = rows[0]
        return ProjectContent(
            caption=row["caption"],
            image_url=row["image_url"],
            id=row["id"],
            project_id=row["project_id"],
        )

    def get_content(self, id: int) -> ProjectContent:
        rows: list[dict] = self._connection.execute(
            "SELECT * FROM project_contents WHERE id = %s",
            [
                id,
            ],
        )
        row: dict = rows[0]
        return ProjectContent(
            project_id=row["project_id"],
            caption=row["caption"],
            image_url=row["image_url"],
            id=row["id"],
        )
