class Sketchbook:
    def __init__(self, image_url: str, id=None) -> None:
        self.id: int = id
        self.image_url: str = image_url

    def __repr__(self):
        return f"Sketchbook({self.id}, {self.image_url!r})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
