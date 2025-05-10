# jpeg_quality.py
# JPEGに圧縮する関数

from PIL import Image
import os

def compress_jpeg_quality(input_path: str, output_path: str = None, quality: int = 30) -> str:
    """
    指定したJPEG品質で画像を圧縮する。

    Parameters:
    - input_path: 元画像のパス
    - output_path: 保存先のパス（省略時は元画像名に _compressed を付ける）
    - quality: JPEGの品質（0-100、小さいほど圧縮率が高く画質が落ちる）

    Returns:
    - output_path: 圧縮後の画像ファイルパス
    """
    if output_path is None:
        base, _ = os.path.splitext(input_path)
        output_path = f"{base}_compressed.jpg"

    img = Image.open(input_path).convert("RGB")  # JPEG用にRGB変換
    img.save(output_path, "JPEG", quality=quality, optimize=True)

    return output_path
