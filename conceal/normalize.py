import os
from PIL import Image
import numpy as np


def normalize(object):
    images = os.listdir(object)
    if not (os.path.isdir(object + "_normalized/")):
        os.mkdir(object + "_normalized/")
    for img in images:
        image = object + "/" + img
        im = Image.open(image)
        sqrWidth = np.ceil(np.sqrt(im.size[0] * im.size[1])).astype(int)
        im_resize = im.resize((400, 400))
        im_resize.save(object + "_normalized/" + img)
        im_resize.close()


def normalize_one(img, path):
    im = Image.open(img)
    sqrWidth = np.ceil(np.sqrt(im.size[0] * im.size[1])).astype(int)
    im_resize = im.resize((1000, 1000))
    im_resize.save(path)
    im_resize.close()
