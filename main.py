import cv2

img = cv2.imread('C:\\Users\\C605\\Desktop\\minecraft.jpg')

blue, green, red = cv2.split(img)

cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)



print(blue)

for i in range(0,700):
    for j in range(0,700):
        blue[i,j] = 10
        green[i,j] = 5
        red[i,j] = 10

merged_img = cv2.merge([blue, green, red])

cv2.imshow('merged',merged_img)

cv2.waitKey(0)