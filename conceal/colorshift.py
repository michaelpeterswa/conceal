from PIL import ImagePalette, Image
import colorsys
import numpy as np


def colorshift(conf, image_palette):

    img = conf["files"]["resultfolder"] + "/" + conf["files"]["noise"]
    im = Image.open(img)
    conv = im.convert("P")
    conv.putpalette(image_palette)
    conv.save(conf["files"]["resultfolder"] + "/" + conf["files"]["colorshift"])
    print("Swapped Color Palettes: ✔")
