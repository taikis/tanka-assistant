from PIL import Image, ImageFont, ImageDraw


class Generator:
    def __init__(
        self,
        text,
        font_path="./font/KouzanBrushFontSousyo.ttf",
        font_size=100,
        image_size=(2480, 3508),
    ):
        self.text = text
        self.font = ImageFont.truetype(font_path, font_size)
        self.image = Image.new("RGB", image_size, (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)

    def draw_text(self):
        self.draw.text((1000, 1000), self.text, font=self.font)

    def save(self, path):
        self.image.save(path)

    def show(self):
        self.image.show()


if __name__ == '__main__':
    generator = Generator("こんにちは")
    generator.draw_text()
    generator.save("test.png")
