import os
from dotenv import load_dotenv
load_dotenv()

import cloudinary
from werkzeug.datastructures import FileStorage

cloudinary.config(
    cloud_name = os.getenv("CLOUD_NAME"),
    api_key = os.getenv("CLOUD_API_KEY"),
    api_secret = os.getenv("CLOUD_API_SECRET")
)

import cloudinary.uploader

class CloudinaryService:
   
    @staticmethod
    def upload(file: FileStorage, asset_folder: str) -> str:
        print(file)
        result = cloudinary.uploader.upload(
            file, 
            asset_folder=asset_folder)
        return result["secure_url"]