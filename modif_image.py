from skimage.transform import swirl
from skimage.io import imread, imsave
from PIL import Image
import numpy as np
import cv2


def tourbillion(path, force) :
    image = imread(path)
    taille = max(image.shape)
    image = swirl(image, rotation=0, strength=force, radius=taille)
    imsave('img.png', image)

def detection(path) :
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('C:/Users/StarS/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')    #'/data/haarcascade_frontalface_alt2.xml'
    # Read the input image
    img = cv2.imread(path)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    return faces
    """for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()"""

def groscerveau(path, coord, force) :
    img = cv2.imread(path)
    x=coord[0][0]
    y=coord[0][1]
    w=coord[0][2]
    h=coord[0][3]
    center = (x+w//2,y)
    radius = w//2
    power = force # >1.0 for expansion, <1.0 for shrinkage

    height, width, _ = img.shape
    map_y = np.zeros((height,width),dtype=np.float32)
    map_x = np.zeros((height,width),dtype=np.float32)

    # create index map
    for i in range(height):
        for j in range(width):
            map_y[i][j]=i
            map_x[i][j]=j

    # deform around the right eye
    for i in range (-radius, radius):
        for j in range(-radius, radius):
            if (i**2 + j**2 > radius ** 2):
                continue

            if i > 0:
                map_y[center[1] + i][center[0] + j] = center[1] + (i/radius)**power * radius
            if i < 0:
                map_y[center[1] + i][center[0] + j] = center[1] - (-i/radius)**power * radius
            if j > 0:
                map_x[center[1] + i][center[0] + j] = center[0] + (j/radius)**power * radius
            if j < 0:
                map_x[center[1] + i][center[0] + j] = center[0] - (-j/radius)**power * radius

    warped=cv2.remap(img,map_x,map_y,cv2.INTER_LINEAR)
    cv2.imwrite('img.png', warped)
