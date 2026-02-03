from lib.project_image import ProjectImage
from lib.database_connection import DatabaseConnection


class ProjectImageRepository:
    def __init__(self, db_connection: DatabaseConnection):
        self._connection = db_connection

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

    def get_project_image(self, id: int) -> ProjectImage:
        rows: list[dict] = self._connection.execute(
            "SELECT * FROM project_images WHERE id = %s; ",
            [
                id,
            ],
        )
        row: dict = rows[0]
        return ProjectImage(
            caption=row["caption"],
            image_url=row["image_url"],
            id=row["id"],
            project_id=row["project_id"],
        )

    def get_all_project_images(self, project_id: int) -> list[ProjectImage]:
        rows: list[dict] = self._connection.execute(
            "SELECT * FROM project_images WHERE project_id = %s", [project_id,]
        )
        print(rows)
        project_images_list: list = []
        for row in rows:
            project_images_list.append(
                ProjectImage(
                    caption=row["id"],
                    image_url=row["image_url"],
                    id=row["id"],
                    project_id=row["project_id"],
                )
            )
        return project_images_list

    def delete_project_image(self, id: int) -> None:
        self._connection.execute(
            "DELETE FROM project_images WHERE id = %s",
            [
                id,
            ],
        )

    def update_image_url(self, id: int, new_image_url: str) -> ProjectImage:
        rows = self._connection.execute(
            "UPDATE project_images SET image_url = %s WHERE id = %s RETURNING *",
            [
                new_image_url,
                id,
            ],
        )
        row: dict = rows[0]
        return ProjectImage(
            caption=row["caption"],
            image_url=row["image_url"],
            id=row["id"],
            project_id=row["project_id"],
        )

    def update_caption(self, id: int, new_caption: str) -> ProjectImage:
        rows: list[dict] = self._connection.execute(
            "UPDATE project_images SET image_url = %s WHERE id = %s RETURNING *",
            [
                new_caption,
                id,
            ],
        )
        row: dict = rows[0]
        return ProjectImage(
            caption=row["caption"],
            image_url=row["image_url"],
            id=row["id"],
            project_id=row["project_id"],
        )
