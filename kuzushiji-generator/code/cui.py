import kuzushiji


def main():
    # 文字を受け取る
    text = input("短歌を入力してください: ")
    generator = kuzushiji.Generator(
        text,
        font_path="./font/KouzanBrushFontSousyo.ttf",
        image_path="./background/japanese-paper_00096.jpg",
    )
    generator.draw_text()
    # 署名を入力してください
    name = input("署名を入力してください: ")
    if name != "":
        generator.sign(
            name,
            "./font/aoyagireisyosimo_ttf_2_01.ttf",
        )
    # ファイル名の入力
    path = input("ファイル名を入力してください: ")
    output_path = generator.save(path)
    print("正常に出力しました。\n" + f"出力先: {output_path}")


if __name__ == "__main__":
    main()
