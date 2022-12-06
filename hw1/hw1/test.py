#'data/train/face/face00051.pgm'
#'data/detect/detectData.txt'
from configparser import Interpolation
import cv2 
import os 
import glob 
from matplotlib import pyplot as plt
import classifier
import numpy as np

datapath = 'data/train'
list_of_t = []
data_layer1 = os.listdir(datapath)
for data_layer2 in data_layer1:
    if data_layer2 == 'face':
        lable = 1
    else:
        lable = 0
    path = os.path.abspath(datapath)
    path = path.replace('\\', '/')
    path = os.path.join(path, data_layer2)
    path = path + "/*.pgm"
    # print(path)
    all_data = glob.glob(path)
    # print(all_data)
    for file in all_data:
        # print(file)
        img = cv2.imread(file, -1)
        t = (img, lable)
        # print(t)
        list_of_t.append(t)
        
print(list_of_t)

plt.imshow(list_of_t[0][0], cmap='gray')
plt.show()


dataPath = 'data/detect/detectData.txt'
rootDir=os.path.abspath(os.path.join(dataPath, os.path.pardir))
jpg = glob.glob(os.path.join(rootDir, "*.jpg"))
#print(jpg)

"""
    image=[]
    image_ans=[]
    for images in jpg:
        tmp= cv2.imread(images,0)
        tmp2=cv2.imread(images)
        #tmp = cv2.cvtColor(tmp, cv2.COLOR_BGR2RGB)
        image.append(tmp)
        image_ans.append(tmp2)
    f = open(dataPath,'rb')
"""

image=cv2.imread(jpg[0],0)#grayscale
image_ans=cv2.imread(jpg[0])#彩色

f = open(dataPath,'rb')
for k in range(len(jpg)):
    small_image_position=[]
    line = f.readline()
    (name, size) = [i for i in line.split()]
    #print(name)
    for i in range(int(size)):
        temp=[]
        line = f.readline()
        for j in line.split():
          temp.append(int(j))
        small_image_position.append(temp)
    for i in jpg:
        name_str=str(name, 'utf-8')
        if name_str==os.path.basename(i):
          image=cv2.imread(i,0) #grayscale
          image_ans=cv2.imread(i) #彩色
          #print("success")
          break
    for i in range(len(small_image_position)):
        x1=small_image_position[i][0]
        y1=small_image_position[i][1]
        x2=small_image_position[i][2]
        y2=small_image_position[i][3]
        smallimage=cv2.resize(image[y1:y1+y2,x1:x1+x2],(19,19),interpolation=cv2.INTER_NEAREST)
        #clf = classifier.WeakClassifier()
        smallimage_array = np.array(smallimage)
        #print(smallimage_array)
        ans = 0
        if ans==1:
          cv2.rectangle(image_ans, (x1, y1), (x2+x1, y2+y1), (0, 255, 0))
        else:
          cv2.rectangle(image_ans, (x1, y1), (x2+x1, y2+y1), (0, 0, 255))
    #cv2.imshow('My Image', image_ans)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows() 



direction = glob.glob(os.path.join('data/train', "*"))
#rootDir = 'data/train'
print(os.path.abspath(os.path.join('data/detect/detectData.txt', os.path.pardir)))
rootDir=os.path.abspath(os.path.join('data/detect/detectData.txt', os.path.pardir))
jpg = glob.glob(os.path.join(rootDir, "*.jpg"))
print(jpg)
for images in jpg:
    image = cv2.imread(images)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #image = cv2.resize(image, (19, 19), interpolation=cv2.INTER_AREA)
    #print(image.shape)
    #plt.imshow(image)
    #plt.show()

f = open('data/detect/detectData.txt','rb')
line = f.readline()
(name, size) = [i for i in line.split()]
print(size)
number1=[]
for i in range(int(size)):
    temp=[]
    line = f.readline()
    for j in line.split():
        temp.append(int(j))
    number1.append(temp)
print(image.shape)
k=0
for i in number1:
    x1=number1[k][0]
    y1=number1[k][1]
    x2=number1[k][2]
    y2=number1[k][3]
    k=k+1
    print((x1,y1,x2,y2))
    smallimage=cv2.resize(image[y1:y1+y2,x1:x1+x2],(19,19),interpolation=cv2.INTER_AREA)
    
    #clf = classifier.WeakClassifier()
    np.array(smallimage)
    ans = 0
    if ans==1:
        cv2.rectangle(image, (x1, y1), (x2+x1, y2+y1), (0, 255, 0))
    else:
        cv2.rectangle(image, (x1, y1), (x2+x1, y2+y1), (255, 0, 0))
    
#cv2.imshow('My Image', image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


        






"""
for lists in os.listdir(rootDir): 
    print(lists)
    path = os.path.join(rootDir, lists) 
    for subpath in os.listdir(path):
        ans = os.path.join(path, subpath) 
        #print(ans)
"""



f = open('data/train/non-face/B1_00011.pgm','rb')
line = f.readline()
line = f.readline()
line = f.readline()
line = f.readline()
#(width, height) = [int(i) for i in line.split()]
print(line)

line = f.readline()
img_dir = "data/train/face/" # Enter Directory of all images  
data_path = os.path.join(img_dir,'*') 
files = glob.glob(data_path) 
data = [] 
for f1 in files: 
    img = cv2.imread(f1) 
    data.append(img) 

# 使用 OpenCV 讀取圖檔
img_bgr = cv2.imread('data/train/non-face/B1_00011.pgm')

# 將 BGR 圖片轉為 RGB 圖片
img_rgb = img_bgr[:,:,::-1]

# 或是這樣亦可
# img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 使用 Matplotlib 顯示圖片
#plt.imshow(img_bgr)
#plt.show()