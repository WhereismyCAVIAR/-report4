import cv2
from matplotlib import pyplot as plt

# 画像のパス
path = '/Users/kakeruyamamori/Desktop/画像処理/report4/2/dora.png'                               
i = cv2.imread(path,0)
# 閾値
th = 127      
# 最大輝度値                                                  
i_max = 255                     
# 二値化処理                                
ret, i_binary = cv2.threshold(i, th, i_max, cv2.THRESH_BINARY)  

#画像の保存
cv2.imwrite('/Users/kakeruyamamori/Desktop/画像処理/report4/2/output_2.jpg', i_binary)

cv2.imshow('binary_image', i_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()