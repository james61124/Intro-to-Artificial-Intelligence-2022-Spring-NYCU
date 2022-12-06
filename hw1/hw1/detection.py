import os
import cv2
import glob
import matplotlib.pyplot as plt
import numpy as np
import adaboost

def detect(dataPath, clf):
    """
    Please read detectData.txt to understand the format. Load the image and get
    the face images. Transfer the face images to 19 x 19 and grayscale images.
    Use clf.classify() function to detect faces. Show face detection results.
    If the result is True, draw the green box on the image. Otherwise, draw
    the red box on the image.
      Parameters:
        dataPath: the path of detectData.txt
      Returns:
        No returns.
    """
    # Begin your code (Part 4)
    # raise NotImplementedError("To be implemented")
    """
    The top number in .txt means how many face we have to detect.
    the following ones means the position of the face, we use cv2.rectangle to draw the rectangle.
    Use classify in clssifier.py to see whether the classifier thinks it is a face.
    To comform to different data in the .txt, 
    I use a for loop to see which image is the one that I have to deal with now.
    It is moe convenient for me to doo part five.

    """
    rootDir=os.path.abspath(os.path.join(dataPath, os.path.pardir))
    jpg = glob.glob(os.path.join(rootDir, "*.jpg"))
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
        ans = clf.classify(smallimage_array)
        if ans==1:
          cv2.rectangle(image_ans, (x1, y1), (x2+x1, y2+y1), (0, 255, 0))
        else:
          cv2.rectangle(image_ans, (x1, y1), (x2+x1, y2+y1), (0, 0, 255))
      cv2.imshow('My Image', image_ans)
      cv2.waitKey(0)
      cv2.destroyAllWindows() 
    
    
    # End your code (Part 4)
