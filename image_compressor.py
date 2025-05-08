import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
FILE_API_URL = f"https://api.telegram.org/file/bot{BOT_TOKEN}"


def download_image(file_id):
    """
    Telegramのfile_idから画像をダウンロードし、そのまま保存
    """
    try:
        # ファイルのパスを取得
        resp = requests.get(f"{API_URL}/getFile?file_id={file_id}")
        resp.raise_for_status()
        file_path = resp.json()["result"]["file_path"]

        # 画像をダウンロード
        file_url = f"{FILE_API_URL}/{file_path}"
        resp = requests.get(file_url)
        resp.raise_for_status()

        # ファイル保存（とりあえずそのまま）
        local_filename = "downloaded_image.jpg"
        with open(local_filename, "wb") as f:
            f.write(resp.content)

        return local_filename

    except requests.exceptions.RequestException as e:
        print(f"エラー: {e}")
        return None