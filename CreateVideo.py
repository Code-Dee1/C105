import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[56])
height, width, channels = frame.shape

output = cv2.VideoWriter("sunrise.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 200, (width, height))

for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    output.write(frame)

output.release()