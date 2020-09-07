import os
from PIL import Image
import numpy as np


def normalize(conf):
    images = os.listdir(conf["files"]["imagefolder"])
    if not (os.path.isdir(conf["files"]["normalized"])):
        os.mkdir(conf["files"]["normalized"])
    for img in images:
        image = conf["files"]["imagefolder"] + "/" + img
        im = Image.open(image)
        sqrWidth = np.ceil(np.sqrt(im.size[0] * im.size[1])).astype(int)
        im_resize = im.resize(
            (conf["normalize"]["height_all"], conf["normalize"]["width_all"])
        )
        im_resize.save(conf["files"]["normalized"] + "/" + img)
        im_resize.close()
    print("Normalized All Images: ✔")


def normalize_one(conf):
    path = conf["files"]["resultfolder"] + "/" + conf["files"]["collage"]
    im = Image.open(path)
    sqrWidth = np.ceil(np.sqrt(im.size[0] * im.size[1])).astype(int)
    im_resize = im.resize(
        (conf["normalize"]["height_one"], conf["normalize"]["width_one"])
    )
    im_resize.save(path)
    im_resize.close()
    print("Normalized Collage Image: ✔")
