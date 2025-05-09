from PIL import Image
import piexif

# 画像を開く
img = Image.open("your_image.jpg")

# EXIFデータがあるか確認
if "exif" in img.info:
    exif_dict = piexif.load(img.info["exif"])

    # 一般的な距離系タグを表示
    for ifd in exif_dict:
        for tag in exif_dict[ifd]:
            tag_name = piexif.TAGS[ifd][tag]["name"]
            print(f"{tag_name}: {exif_dict[ifd][tag]}")
else:
    print("EXIFデータなし")