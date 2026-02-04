class ProjectContent:
    def __init__(
        self, project_id: int, caption: str, image_url: str, id: int = None
    ) -> None:
        self.id: int = id
        self.caption: str = caption
        self.image_url: str = image_url
        self.project_id: int = project_id

    def __repr__(self):
        return f"ProjectContent({self.id}, {self.caption!r}, {self.image_url!r}, {self.project_id})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
