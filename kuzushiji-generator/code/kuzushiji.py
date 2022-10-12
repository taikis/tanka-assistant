from PIL import Image, ImageFont, ImageDraw


class Generator:
    def __init__(
        self,
        text,
        font_path="./font/KouzanBrushFontSousyo.ttf",
        font_size=300,
        image_size=(2480, 3508),
    ):
        # テキストを空白で分割
        self.__text = text.split()
        self.font = ImageFont.truetype(font_path, font_size)
        self.image = Image.new("RGB", image_size, (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)

    def draw_text(
        self,
        margin=None,
        line_spacing=None,
    ):
        # 余白
        if margin is None:
            margin = self.image.size[0] * 0.1
        # 行間
        if line_spacing is None:
            line_spacing = self.font.size * 0.2  # 行間

        # センタリングするために、右端を求める
        text_len = len(self.__text)
        right_edge = (
            self.image.size[0]
            + (self.font.size * text_len + line_spacing * (text_len - 1))
        ) / 2
        # 各行がいい感じになるようにインデントを作成
        indent = [
            0,
            2,
            4,
            1,
            3,
        ]
        # 分割した文章を上記四角形内に左にずらしながら縦書き入力する
        for index, item in enumerate(self.__text):
            self.draw.text(
                (
                    right_edge
                    - (self.font.size / 2)
                    - self.font.size * index
                    - (line_spacing * index),
                    margin + (self.font.size * indent[index]),
                ),
                item,
                fill="black",
                anchor="mt",
                font=self.font,
                direction="ttb",
            )

    def stamp(
        self,
        name,
        font=None,
    ):
        if font is None:
            font = ImageFont.truetype(self.font.path, int(self.font.size * 0.5))

        self.draw.text(
            (self.image.size[0] * 0.1, self.image.size[1] * 0.85),
            name,
            fill="black",
            anchor="lt",
            font=font,
            direction="ttb",
        )

    def save(self, path):
        self.image.save(path)

    def show(self):
        self.image.show()


if __name__ == "__main__":
    generator = Generator("東風吹かば にほひをこせよ 梅の花 主なしとて 春を忘るな")
    generator.draw_text()
    generator.stamp("菅原")
    generator.save("./output/test.png")
