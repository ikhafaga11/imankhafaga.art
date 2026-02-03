class ProjectImage:
    def __init__(self, caption, image_url):
        self.caption = caption
        self.image_url = image_url

    def __repr__(self):
        return f"ProjectImage({self.caption}, {self.image_url})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
