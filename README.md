## 短歌画像生成ソフト

短歌を入力するとくずし字にして画像化します。

## 使い方

**サウンドインターフェースの共有**
1. `brew install pulseaudio`
1. `$ pulseaudio --load=module-native-protocol-tcp --exit-idle-time=-1 --daemon`

**環境の立ち上げ**  
1. Dockerをインストール
1. `make up`

**短歌画像の生成**
1. `make tanka`
1. CUIに従って短歌を作成（短歌は空白区切りで入力してください）
1. `./kuzushiji-generator/code/output/`に生成されます

## 使わせていただいた素材

### 衡山毛筆フォント草書

青柳衡山様  
https://opentype.jp/kouzansousho.htm  

### 青柳隷書しも

青柳衡山様  
SIMO様  
https://opentype.jp/aoyagireisho.htm  
[フォントの使用方法と、フォントの解説](./aoyagireisho-info)

### 和紙画像

ベイツ・イメージズ  
https://www.beiz.jp/