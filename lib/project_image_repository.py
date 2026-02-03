from lib.project_image import ProjectImage;

class ProjectImageRepository:
    def __init__(self, db_connection):
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

    def get_poject_image(self, id: int) -> ProjectImage:
        rows: list[dict] = self._connection.execute(
            "SELECT * FROM project_images WHERE id = %s RETURNING *; ",
            [
                id,
            ],
        )
        row: list = rows[0]
        return ProjectImage(
            caption=row["caption"],
            image_url=row["image_url"],
            id=row["id"],
            project_id=row["project_id"],
        )

    def get_all_project_images(self) -> list[ProjectImage]:
        rows: list[dict] = self._connection.execute(
            "SELECT * FROM project_images RETURNING *;"
        )
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
        rows = self._connection.execute(
            "DELETE FROM project_images WHERE id = %s",
            [
                id,
            ],
        )