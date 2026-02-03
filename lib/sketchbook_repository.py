from lib.sketchbook import Sketchbook
from lib.database_connection import DatabaseConnection


class SketchbookRepository:
    def __init__(self, db_connection: DatabaseConnection):
        self._connection = db_connection

    def add_sketch(self, image_url: str) -> Sketchbook:
        rows: list[dict] = self._connection.execute(
            "INSERT INTO sketchs (image_url) VALUES ( %s ) RETURNING *",
            [
                image_url,
            ],
        )
        row: dict = rows[0]
        return Sketchbook(image_url=row["image_url"], id=row["id"])

    def delete_sketch(self, id: int) -> None:
        self._connection.execute(
            "DELETE FROM sketchs WHERE id = %s",
            [
                id,
            ],
        )

    def get_all_sketches(self) -> list[Sketchbook]:
        rows: list[dict]  = self._connection.execute("SELECT * FROM sketchs")
        sketches_list: list[Sketchbook] = []
        for row in rows:
            sketches_list.append(Sketchbook(row["image_url"]))
        return sketches_list
