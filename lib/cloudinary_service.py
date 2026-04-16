import os
from dotenv import load_dotenv
load_dotenv()

import cloudinary
import werkzeug

cloudinary.config(
    cloud_name = os.getenv("CLOUD_NAME"),
    api_key = os.getenv("CLOUD_API_KEY"),
    api_secret = os.getenv("CLOUD_API_SECRET")
)

import cloudinary.uploader

class CloudinaryService:
    def __init__(self, file: werkzeug.datastructures.file_storage.FileStorage) -> None:
        self.file: werkzeug.datastructures.file_storage.FileStorage = file
    
    def upload(self):
        upload = cloudinary.uploader.upload(self.file)
        return upload

    def __repr__(self):
        return f"CloudinaryService({self.file})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__