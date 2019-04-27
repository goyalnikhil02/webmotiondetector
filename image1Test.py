import cv2

# resize and color change
image = cv2.imread("images/nikhil.jpeg")

cv2.imshow("Original", image)
#print(image.shape)
cv2.waitKey(2000)

#resize_image=cv2.resize(image,(500,500))
# here we half the size of image
resize_image=cv2.resize(image,(int(image.shape[0]/2),int(image.shape[1]/2)))

grayimage = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Hello", grayimage)

cv2.waitKey(2000)

cv2.destroyAllWindows()
