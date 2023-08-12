import io
import os
import requests
from base64 import b64decode
from PIL import Image
import logging

logger = logging.getLogger(__name__)

# Fetching configurations from environment variables
SD_WEBUI_AUTH = os.environ.get('SD_WEBUI_AUTH')
SD_WEBUI_URL = os.environ.get('SD_WEBUI_URL')

def create_session(username: str = "", password: str = ""):
    s = requests.Session()
    if username and password:
        s.auth = (username, password)
    return s

def save_image(b64_data: str, filename: str):
    b64 = b64decode(b64_data.split(",", 1)[0])
    image = Image.open(io.BytesIO(b64))
    image.save(filename)
    logger.info(f"Saved to disk:{filename}")
    return f"Saved to disk:{filename}"

def generate_image_with_sd_webui(
    prompt: str,
    filename: str,
    size: int = 512,
    negative_prompt: str = "",
    extra: dict = {}
) -> str:
    
    # Splitting auth if provided
    username, password = "", ""
    if SD_WEBUI_AUTH:
        auth_parts = SD_WEBUI_AUTH.split(":")
        username = auth_parts[0]
        password = auth_parts[1] if len(auth_parts) > 1 else ""


    session = create_session(username, password)

    response = session.post(
        f"{SD_WEBUI_URL}/sdapi/v1/txt2img",
        json={
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "sampler_index": "DDIM",
            "steps": 20,
            "config_scale": 7.0,
            "width": size,
            "height": size,
            "n_iter": 1,
            **extra,
        },
    )
    
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    
    response_data = response.json()
    if "images" not in response_data or not response_data["images"]:
        raise ValueError("Unexpected response data")
    
    logger.info(f"Image Generated for prompt:{prompt}")

    return save_image(response_data["images"][0], filename)


generate_image_with_sd_webui(
    'a grassy field',
    './pictures/picture.jpg',
    512,
    ""
)