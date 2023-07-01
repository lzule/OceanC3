import os
import cv2
root_path = 'F:/2023OceanCompit/C3/C3-1/video_test'
video_list = os.listdir(root_path)
if not os.path.isdir('./test_photo'):
    os.mkdir('./test_photo')
# print(video_list)
num = 0
for video_name in video_list:
    cap=cv2.VideoCapture(os.path.join(root_path, video_name))
    _, photo = cap.read()
    while True:
        ret, frame = cap.read()
        cv2.waitKey(30)
        if not ret:
            num += 1
            cv2.imwrite('./test_photo/' + video_name + '.jpg', photo)
            break
        photo = frame
print(num)