import os
import requests

# 環境変数の取得（統一を確認）
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
        file_data = resp.json()

        # エラーハンドリング（APIレスポンスに result があるか確認）
        if "result" not in file_data or "file_path" not in file_data["result"]:
            print("エラー: ファイル情報が取得できませんでした。")
            return None

        file_path = file_data["result"]["file_path"]

        # 画像をダウンロード
        file_url = f"{FILE_API_URL}/{file_path}"
        resp = requests.get(file_url)
        resp.raise_for_status()

        # ファイル保存（そのまま）
        local_filename = "downloaded_image.jpg"
        with open(local_filename, "wb") as f:
            f.write(resp.content