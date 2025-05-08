#ダミー圧縮処理
import os
import requests

BOT_TOKEN = os.getenv("IMGCOMP_BOT_TOKEN")
FILE_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/getFile"
DOWNLOAD_URL = f"https://api.telegram.org/file/bot{BOT_TOKEN}"

def compress_image(file_id):
    """
    ダミーの圧縮処理：Telegramから画像を取得し、保存するだけ
    """
    try:
        # Telegramからファイルパスを取得
        res = requests.get(FILE_API_URL, params={"file_id": file_id})
        res.raise_for_status()
        file_path = res.json()["result"]["file_path"]

        # 画像をダウンロード
        file_url = f"{DOWNLOAD_URL}/{file_path}"
        img_data = requests.get(file_url)
        img_data.raise_for_status()

        # 保存先のファイルパス
        save_path = f"compressed_{os.path.basename(file_path)}"
        with open(save_path, "wb") as f:
            f.write(img_data.content)

        return save_path
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to compress image: {e}")
