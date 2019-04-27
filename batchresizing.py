import cv2
import glob
import os
# resize and color change


#1st way

path= glob.glob("sample-images/*.jpg")
images = []

for img in path:
    n = cv2.imread(img)
    images.append(n)
    

'''
# 2nd way
images = [cv2.imread(file) for file in glob.glob("sample-images/*.jpg")]
print(len(images))

'''


'''
3 rd way to read the multiple files
data_path = os.path.join('sample-images','*g')
files = glob.glob(data_path)
data = []
for f1 in files:
    img = cv2.imread(f1)
    data.append(img)

print(len(data))
'''
i=0
for image in images:
    #image=cv2.imread(img)
    cv2.imshow("Original", image)
    cv2.waitKey(2000)
    #resize_image=cv2.resize(image,(500,500))
    # here we half the size of image
    resize_image=cv2.resize(image,(int(image.shape[0]/2),int(image.shape[1]/2)))
    grayimage = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Hello", grayimage)

    #print(type(name))
    cv2.imwrite("resized_"+str(i)+".jpg", grayimage)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    i=i+1
    #cv2.imwrite("image", grayimage)
