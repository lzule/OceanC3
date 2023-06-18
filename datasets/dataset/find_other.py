import os
import cv2


image1_list = os.listdir('./Coast_Barrier/JPEGImages')

image2_list = os.listdir('./Coast_Barrier/Annotations')

if not os.path.exists('../cocoC3/test/'):
    os.makedirs('../cocoC3/test/')

num = 0
for image in image1_list:
    if image[:-4] + '.xml' not in image2_list:
        print(image)
        cv2.imwrite('../cocoC3/test/' + image, cv2.imread('./Coast_Barrier/JPEGImages/' + image))
        num += 1

print(num)