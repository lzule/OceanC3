import cv2
import os
root_path = 'F:/2023OceanCompit/C3/C3-1/videos_train'
mp4_list = os.listdir(root_path)

if not os.path.isdir('./train_img'):
    os.mkdir('./train_img')
# print(video_list)
num = 0
for video_name in mp4_list:
    cap = cv2.VideoCapture(os.path.join(root_path, video_name))
    print(video_name)
    num_test = 0
    num_1 = 0
    while True and num_test < 50:
        ret, frame = cap.read()
        cv2.waitKey(33)
        num_1 += 1
        if ret and num_1 % 3 == 0:
            num_test += 1
            print(num_test)
            cv2.imwrite('./train_img/' + video_name.split('.')[-2] + '_' + str(num_test) + '.jpg', frame)
        if not ret:
            break
print(num)
