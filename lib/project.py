class Project:
    def __init__(self, title, cover_image_url, id=None):
        self.id = id
        self.title = title
        self.cover_image_url = cover_image_url
        self.images = []

    def __repr__(self):
        return f"Project({self.id}, {self.title!r}, {self.cover_image_url!r}, {self.images})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
