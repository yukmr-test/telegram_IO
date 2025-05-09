from PIL import Image

def compress_by_resizing(input_path: str, output_path: str, scale: float = 0.5):
    """
    指定倍率で画像をリサイズして保存する（例：scale=0.5で50%サイズ）

    Args:
        input_path (str): 入力画像のファイルパス
        output_path (str): 出力画像のファイルパス
        scale (float): 縮小倍率（0 < scale <= 1.0）
    """
    with Image.open(input_path) as img:
        original_size = img.size
        new_size = (int(original_size[0] * scale), int(original_size[1] * scale))
        resized_img = img.resize(new_size, Image.LANCZOS)
        resized_img.save(output_path, format="JPEG", quality=85)
        print(f"Resized from {original_size} to {new_size} and saved to {output_path}")
