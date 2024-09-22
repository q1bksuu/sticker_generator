from PIL import Image, ImageDraw, ImageFont

from sticker_generator.settings import BASE_DIR

img_ins = Image.open(BASE_DIR.joinpath('static/image/heart_empty.jpg'), formats=['jpeg'])

fontSize = 45
font = ImageFont.truetype(
    BASE_DIR.joinpath('static/font/SourceHanSans/OTF/SimplifiedChinese/SourceHanSansSC-Bold.otf'), fontSize)


def generate(text: str, angle: float, io_stream):
    img = img_ins.copy()

    text_img = Image.new("RGBA", (int(font.getlength(text)), font.font.height), (0, 0, 0, 0))

    text_draw = ImageDraw.Draw(text_img)
    text_draw.text((0, 0), text, font=font, fill=(161, 0, 0))
    text_img = text_img.rotate(-angle, resample=Image.Resampling.BICUBIC, expand=True)

    x = 130 - text_img.width // 2
    y = 52 - text_img.height // 2
    img.paste(text_img, (x, y), text_img)
    img.save(io_stream, format='jpeg')
