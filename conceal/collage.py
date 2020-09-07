# Makes a collage image from a directory full of images
#
# adapted from https://gist.github.com/jgrahamc/8b615ca48b2c89dc5a1a19a3bc5bfa17
#
# Assumes all the images are the same size and square

import os
from PIL import Image
import random
import math


def collage(conf):
    images = os.listdir(conf["files"]["normalized"])

    if not (os.path.isdir(conf["files"]["resultfolder"])):
        os.mkdir(conf["files"]["resultfolder"])

    aspect = 1.77  # Aspect ratio of the output image

    cols = int(math.sqrt(len(images) * aspect))
    rows = int(math.ceil(float(len(images)) / float(cols)))

    random.shuffle(images)
    (w, h) = (conf["collage"]["height"], conf["collage"]["width"])

    (width, height) = (w * cols, h * rows)

    collage = Image.new("RGB", (width, height))
    for y in range(rows):
        for x in range(cols):
            i = y * cols + x
            # Fill in extra images by duplicating some images randomly
            if i >= len(images):
                i = random.randrange(len(images))
            p = Image.open(conf["files"]["normalized"] + "/" + images[i])
            collage.paste(p, (x * w, y * h))
            p.close()
    collage.save(conf["files"]["resultfolder"] + "/" + conf["files"]["collage"])
    collage.close()
    print("Created Collage: ✔")
