#画像の受け渡し処理

import os
import requests

# 環境変数の取得（修正済み）
BOT_TOKEN = os.getenv("IMGCOMP_BOT_TOKEN")  
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def extract_message_info(data):
    """
    TelegramのWebhookデータからメッセージとchat_idを抽出
    """
    try:
        message = data.get("message")
        if not message:
            return None, None
        chat_id = message["chat"]["id"]
        return message, chat_id
    except Exception as e:
        print(f"[extract_message_info ERROR] {e}")
        return None, None

def send_text_message(chat_id, text):
    """
    テキストメッセージを送信
    """
    url = f"{API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[send_text_message ERROR] {e}")

def send_photo_message(chat_id, photo_path):
    """
    圧縮後の画像ファイルを送信
    """
    url = f"{API_URL}/sendPhoto"
    try:
        with open(photo_path, 'rb') as photo_file:
            files = {'photo': photo_file}
            data = {'chat_id': chat_id}
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[send_photo_message ERROR] {e}")