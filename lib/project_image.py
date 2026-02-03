class ProjectImage:
    def __init__(self, caption, image_url, id=None, project_id=None):
        self.id = id
        self.caption = caption
        self.image_url = image_url
        self.project_id = project_id

    def __repr__(self):
        return f"ProjectImage({self.id}, {self.caption!r}, {self.image_url!r}, {self.project_id})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
