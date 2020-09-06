from PIL import ImagePalette, Image
import colorsys
import numpy as np


def colorshift(conf, image_palette, image_to_quant, save):

    img = image_to_quant
    im = Image.open(img)
    conv = im.convert("P")
    conv.putpalette(image_palette)
    conv.save(save)
