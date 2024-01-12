import numpy as np
import cv2
from matplotlib import pyplot as plt
 
## 画像から輪郭を検出する関数
def contours(img):
    # グレースケール化
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 二値化
    ret, img_binary = cv2.threshold(img_gray,
                                    # 二値化のための閾値60(調整要)
                                    60, 255,
                                    cv2.THRESH_BINARY)
    # 輪郭検出
    contour_list, hierarchy = cv2.findContours(img_binary,
                                           # すべての輪郭を抽出し、階層構造を無視してリストにする
                                           cv2.RETR_LIST,
                                           cv2.CHAIN_APPROX_SIMPLE)
    # 輪郭情報をndarrayに変換
    contours_array = [np.array(contour) for contour in contour_list]
    # 輪郭のx方向平均値を算出
    x = np.mean(contours_array[0].T[0, 0])
    # 輪郭のy方向平均値を算出
    y = np.mean(contours_array[0].T[1, 0])
    return x, y

# 動画ファイルの読み込み
movie = cv2.VideoCapture('/Users/kakeruyamamori/Desktop/画像処理/report4/testmovie1.avi')

# 動画ファイル保存用の設定
fps = int(movie.get(cv2.CAP_PROP_FPS))             # 動画のFPSを取得
w = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))       # 動画の横幅を取得
h = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))      # 動画の縦幅を取得
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')# 動画保存時のfourcc設定（mp4用）
# 動画の仕様（ファイル名、fourcc, FPS, サイズ, カラー）
video = cv2.VideoWriter(
                        '/Users/kakeruyamamori/Desktop/画像処理/report4/6/output_6.mp4',
                        fourcc, fps, (w, h), True
                        )
 
# ファイルからフレームを1枚ずつ取得して動画処理後に保存する
x_list = []
y_list = []
while True:
    ret, frame = movie.read()                      # フレームを取得
 
    # フレームが取得できない場合はループを抜ける
    if not ret:
        break
 
    x, y = contours(frame)                         # 輪郭検出から物体中心を算出
 
    # スナイパーマークのパラメータ
    center_point = (int(x), int(y))  # 中心点
    mark_color = (255, 0, 0)  # 色 (赤)
    mark_thickness = 2  # 線の太さ
    radius = 10  # 中心円の半径
    line_length = 20  # 線の長さ

    # スナイパーマークの描画
    cv2.circle(frame, center_point, radius, mark_color, -1)  # 中心の円
    cv2.line(frame, (center_point[0] - line_length, center_point[1]), (center_point[0] + line_length, center_point[1]), mark_color, mark_thickness)  # 横線
    cv2.line(frame, (center_point[0], center_point[1] - line_length), (center_point[0], center_point[1] + line_length), mark_color, mark_thickness)  # 縦線

    # テキストの追加
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'target', (center_point[0] - 30, center_point[1] + 40), font, 0.5, mark_color, 1, cv2.LINE_AA)


 
    video.write(frame)  # 動画を保存する
    x_list.append(x)
    y_list.append(y)
 
# 動画オブジェクト解放
movie.release()