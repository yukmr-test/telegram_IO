#圧縮呼び出し口（エントリーポイント）こいつを起動して対象を圧縮する
from compression_methods.jpeg_quality import compress_jpeg_quality

def compress_image(input_path: str, method: str = "jpeg", output_path: str = None) -> str:
    if method == "jpeg":
        return compress_jpeg_quality(input_path, output_path)
    else:
        raise ValueError(f"Unsupported compression method: {method}")

# テスト用実行
if __name__ == "__main__":
    input_file = "sample.jpg"  # 任意の画像ファイルを配置してね
    output = compress_image(input_file)
    print(f"Compressed image saved at: {output}")
