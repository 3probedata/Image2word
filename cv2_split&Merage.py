import cv2
img = cv2.imread("p1.jpg")
point1 = (0, 0)
point2 = (200,200)
crop_img = img[point1[1]:point2[1], point1[0]:point2[0]] #取影像
cv2.imshow('img',img)

img2 = cv2.hconcat([crop_img, crop_img]) # H水平
img3 = cv2.vconcat([crop_img, crop_img]) # V垂直
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()