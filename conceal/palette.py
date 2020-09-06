from colorthief import ColorThief
import numpy as np
from PIL import Image


def generate(conf, image, save):
    color_thief = ColorThief(image)

    # https://stackoverflow.com/questions/56069551/trying-to-display-list-of-rgb-values
    barColors = color_thief.get_palette(color_count=conf["palette"]["colors"])
    barColors = (np.array(barColors)).astype(np.uint8)
    cols = len(barColors)
    rows = max([1, int(cols / 2.5)])

    # Create color Array
    barFullData = np.tile(barColors, (rows, 1)).reshape(rows, cols, 3)
    # Create Image from Array
    barImg = Image.fromarray(barFullData, "RGB")

    # saving image
    barImg.save(save)

    return barColors
