import cv2

face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt2.xml")

image = cv2.imread("images/tv.jpeg")#to detect the face from tv pics

#image = cv2.imread("images/image3.jpeg")#group pics
#image = cv2.imread("images/nikhil.jpeg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5) #try scalefoactor=1.05
for x, y, w, h in faces:
    img=cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)# srcimage,starting point ,endpoint,color of rect ,width
    #img_gray = cv2.rectangle(gray_image, (x, y), (x + w, y + h), (0, 255, 0),
 #                            3)  # srcimage,starting point ,endpoint,color of rect ,width

print("Face Count: ",len(faces))
resize_image=cv2.resize(img,(int(img.shape[0]/3),int(img.shape[1]/3)))

cv2.imshow("Face detected", resize_image)
key=cv2.waitKey(2000)
#if key ==
cv2.destroyAllWindows()
