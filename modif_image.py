from skimage.transform import swirl
from skimage.io import imread, imsave
from skimage.transform import PiecewiseAffineTransform, warp
from PIL import Image
import numpy as np
import cv2
import os
from glitch_this import ImageGlitcher

import gifsize

def compress_image(path) :
    img = Image.open(path)
    img = img.convert('RGB')

    #rot = random.random()*10

    img = img.resize((img.size[0]//15,img.size[1]//15))
    #img = img.rotate(rot, expand=True)
    img = img.resize((img.size[0]*15,img.size[1]*15))
    #img = img.rotate(360 + rot, expand=True)

    img.save(path, quality=1)

def tourbillion(path, force) :
    if path.endswith(".gif") :
        img = Image.open(path)
        nbFrames = img.n_frames
        try :
            duration = img.info['duration']
        except :
            duration = 40

        if ":" in force :
            _min=int(force.split(":")[0])
            _max=int(force.split(":")[-1])
            f=np.linspace(_min,_max,nbFrames)
        else :
            f=[int(force) for i in range(nbFrames)]

        for frame in range(0, nbFrames) :
            img.seek(frame)
            img.save(str(frame)+".gif")

        for frame in range(0, nbFrames) :
            image = imread(str(frame)+".gif")
            taille = max(image.shape)
            image = swirl(image, rotation=0, strength=f[frame], radius=taille)
            image = 255 * image
            imsave(str(frame)+".gif", image.astype(np.uint8))

        images = []
        for frame in range(0, nbFrames) :
            im = Image.open(str(frame)+".gif")
            images.append(im)

        images[0].save('anim.gif', save_all=True, append_images=images[1:], optimize=False, duration=duration, loop=0)

        while os.path.getsize('anim.gif') > 8e+6 :
            gifsize.resize_gif('anim.gif', duration=duration)

        return nbFrames

    else :
        image = imread(path)
        taille = max(image.shape)
        image = swirl(image, rotation=0, strength=force, radius=taille)
        image = 255 * image
        imsave('img.png', image.astype(np.uint8))
        return

def glitch(path, force) :
    glitcher = ImageGlitcher()
    glitch_img = glitcher.glitch_image(path, force, color_offset=True, gif=True)
    glitch_img[0].save('glitched.gif', format='GIF', append_images=glitch_img[1:], save_all=True, duration=200, loop=0)

def blob(path = 'img.png') :
    im = Image.open(path)
    image = np.array(im)
    rows, cols = image.shape[0], image.shape[1]

    src_cols = np.linspace(0, cols, 20)
    src_rows = np.linspace(0, rows, 10)
    src_rows, src_cols = np.meshgrid(src_rows, src_cols)
    src = np.dstack([src_cols.flat, src_rows.flat])[0]

    # add sinusoidal oscillation to row coordinates
    dst_rows = src[:, 1] - np.sin(np.linspace(np.pi, 2*np.pi, src.shape[0])) * 50
    dst_cols = src[:, 0]
    dst_rows *= 1.5
    dst_rows -= 1.5 * 50
    dst = np.vstack([dst_cols, dst_rows]).T


    tform = PiecewiseAffineTransform()
    tform.estimate(src, dst)

    out_rows = image.shape[0] - 1.5 * 50
    out_cols = cols
    out = warp(image, tform, output_shape=(out_rows, out_cols))

    im = Image.fromarray((out * 255).astype(np.uint8))
    im.save("img.png")

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