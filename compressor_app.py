# Falksでwebhookの画像を受け取り、image_compressor.pyに受け渡す部分

from flask import Flask, request
import os
from utils.telegram_io import extract_message_info, send_photo_message, send_text_message
from image_compressor import compress_image  # ダミー処理でもOK
from dotenv import load_dotenv

load_dotenv()
IMGCOMP_BOT_TOKEN = os.getenv("IMGCOMP_BOT_TOKEN")

app = Flask(__name__)

@app.route('/')
def index():
    return "Image Compression Bot is running", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message, chat_id = extract_message_info(data)

    if not message or not chat_id:
        return "No valid message", 200

    if "photo" in message:
        file_id = message["photo"][-1]["file_id"]
        try:
            compressed_path = compress_image(file_id)
            send_photo_message(chat_id, compressed_path)
        except Exception as e:
            print(f"[compress_image ERROR] {e}")
            send_text_message(chat_id, "画像処理に失敗しました。")
    else:
        send_text_message(chat_id, "画像を送ってください。")

    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Renderが自動で指定するポートを取得
    app.run(host="0.0.0.0", port=port)
