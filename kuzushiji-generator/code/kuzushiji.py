from PIL import Image, ImageFont, ImageDraw
import math
import datetime

class Generator:
    def __init__(
        self,
        text,
        image_path=None,
        font_path="./font/KouzanBrushFontSousyo.ttf",
        font_size=300,
        image_size=(2480, 3508),
    ):
        # テキストを空白で分割
        self.__text = text.split()
        self.font = ImageFont.truetype(font_path, font_size)
        if image_path is None:
            self.image = Image.new("RGB", image_size, (255, 255, 255))
        else:
            self.image = self.trimming_background(image_path, image_size)
        self.draw = ImageDraw.Draw(self.image)

    def trimming_background(self, image_path, image_size):
        background_image = Image.open(image_path)
        magnification = 1
        for index in range(2):
            if background_image.size[index] < image_size[index]:
                magnification = image_size[index] / background_image.size[index]
                background_image = background_image.resize(
                    size=(
                        math.ceil(background_image.size[0] * magnification),
                        math.ceil(background_image.size[1] * magnification),
                    )
                )

        background_image = background_image.convert("RGB")
        background_image = background_image.crop((0, 0, image_size[0], image_size[1]))
        return background_image

    def draw_text(
        self,
        margin=None,
        line_spacing=None,
    ):
        # 余白
        if margin is None:
            margin = self.image.size[0] * 0.15
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
        font_path=None,
    ):
        if font_path is None:
            font_path = self.font.path
        font = ImageFont.truetype(font_path, int(self.font.size * 0.5))

        self.draw.text(
            (self.image.size[0] * 0.1, self.image.size[1] * 0.8),
            name,
            fill="red",
            anchor="lt",
            font=font,
            direction="ttb",
        )

    def save(
        self,
        path=None,
    ):
        if path is None or path == "":
            #日付時刻からファイル名を生成
            now = datetime.datetime.now()
            path = f"./output/out-{now.strftime('%Y%m%d%H%M%S')}.png"
        self.image.save(path)
        return path

    def show(self):
        self.image.show()


if __name__ == "__main__":
    """
    テスト用短歌
    意味: 進捗を作らなくてはいけないと思いつつ、手が進まない。気付けば夜は明け、真っ白なディスプレイが目に入る。
    """
    generator = Generator(
        text="進捗や 作らなくてはと 白々明け されど目の前 銀雪の画面",
        image_path="./background/japanese-paper_00096.jpg",
    )
    generator.draw_text()
    generator.stamp(
        "菅原",
        "./font/aoyagireisyosimo_ttf_2_01.ttf",
    )
    generator.save("./output/test.png")
