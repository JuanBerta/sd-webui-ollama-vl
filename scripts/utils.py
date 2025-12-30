import ollama
import base64
from io import BytesIO
from PIL import Image

def get_local_models():
    try:
        response = ollama.list()
        models = response.get("models", [])
        models_list = [model["model"] for model in models]
        return sorted(models_list) if models_list else ["No model detected"]
    except Exception:
        return ["No model detected"]

def pil_to_base64(pil_image):
    """
    Converts a single PIL image from Forge into a base64 string.
    """
    if pil_image is None:
        return None
    
    # Ensure RGB to avoid alpha channel issues
    if pil_image.mode != "RGB":
        pil_image = pil_image.convert("RGB")
        
    buffer = BytesIO()
    pil_image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")