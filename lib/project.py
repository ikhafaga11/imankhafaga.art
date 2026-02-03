class Project:
    def __init__(self, title, cover_image):
        self.title = title
        self.cover_image = cover_image
        self.images = []

    def __repr__(self):
        return f"Project({self.title}, {self.cover_image}, {self.images})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
