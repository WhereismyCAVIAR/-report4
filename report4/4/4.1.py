import cv2
from matplotlib import pyplot as plt
 
# カラー画像の読み込み
img = cv2.imread('/Users/kakeruyamamori/Desktop/画像処理/report4/4/dora.png', 1)
 
# ノイズ除去
img_blur = cv2.GaussianBlur(img, (5, 5), 0)

# グレースケール化
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

# エッジ強調
edges = cv2.Canny(img_gray, 50, 150)

# 単純二値化
ret, img_binary = cv2.threshold(edges, 60, 255, cv2.THRESH_BINARY)

# 輪郭抽出
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 輪郭を元画像に描画
img_contour = cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
 
#画像を保存
cv2.imwrite('/Users/kakeruyamamori/Desktop/画像処理/report4/4/output_4.1.jpg', img_contour)

# ここから画像描画
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.imshow(cv2.cvtColor(img_contour, cv2.COLOR_BGR2RGB))
ax1.axis('off')
plt.show()
plt.close()