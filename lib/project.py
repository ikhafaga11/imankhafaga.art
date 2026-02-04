from lib.project_content import ProjectContent


class Project:
    def __init__(self, title: str, cover_image_url: str, id=None) -> None:
        self.id: int = id
        self.title: str = title
        self.cover_image_url: str = cover_image_url
        self.contents: list[ProjectContent] = []

    def add_content(self, content: ProjectContent) -> None:
        self.contents.append(content)

    def remove_content(self, content: ProjectContent) -> None:
        self.contents.remove(content)

    def __repr__(self):
        return f"Project({self.id}, {self.title!r}, {self.cover_image_url!r}, {self.contents})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
