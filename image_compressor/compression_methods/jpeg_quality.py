#jpegに圧縮するやつ

from PIL import Image
import os

def compress_jpeg_quality(input_path: str, output_path: str = None, quality: int = 30) -> str:
    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_compressed.jpg"

    img = Image.open(input_path).convert("RGB")
    img.save(output_path, "JPEG", quality=quality, optimize=True)

    return output_path
