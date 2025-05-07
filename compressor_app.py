from flask import Flask, request
import os
from utils.telegram_io import extract_message_info, send_photo_message, send_text_message
from image_compressor import compress_image  # 後で作成予定
from dotenv import load_dotenv

load_dotenv()
IMGCOMP_BOT_TOKEN= = os.getenv("INMGCOMP_BOT_TOKENI")

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

    # 写真の処理（画像付きメッセージであるかチェック）
    if "photo" in message:
        # Telegramは複数サイズで送ってくる → 最後の（最大サイズ）を選ぶ
        file_id = message["photo"][-1]["file_id"]
        try:
            compressed_file = compress_image(file_id)  # file_id を使って画像取得 → 圧縮
            send_photo_message(chat_id, compressed_file)
        except Exception as e:
            send_text_message(chat_id, "画像処理に失敗しました。")
            print(f"[ERROR] {e}")
    else:
        send_text_message(chat_id, "画像を送ってください。")

    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
