import os
from dotenv import load_dotenv
load_dotenv()

import cloudinary

cloudinary.config(
    cloud_name = os.getenv("CLOUD_NAME"),
    api_key = os.getenv("CLOUD_API_KEY"),
    api_secret = os.getenv("CLOUD_API_SECRET")
)
import cloudinary.uploader
import cloudinary.api

# Import the CloudinaryImage and CloudinaryVideo methods for the simplified syntax used in this guide
from cloudinary import CloudinaryImage
from cloudinary import CloudinaryVideo

print(cloudinary.uploader.upload("./assets/images/about-us (1).png"))
