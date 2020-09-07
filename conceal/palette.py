from colorthief import ColorThief
import numpy as np
from PIL import Image


def generate(conf):
    color_thief = ColorThief(
        conf["files"]["resultfolder"] + "/" + conf["files"]["collage"]
    )

    # https://stackoverflow.com/questions/56069551/trying-to-display-list-of-rgb-values
    barColors = color_thief.get_palette(color_count=conf["colors"]["palette"])
    barColors = (np.array(barColors)).astype(np.uint8)
    cols = len(barColors)
    rows = max([1, int(cols / 2.5)])

    # Create color Array
    barFullData = np.tile(barColors, (rows, 1)).reshape(rows, cols, 3)
    # Create Image from Array
    barImg = Image.fromarray(barFullData, "RGB")

    # saving image
    barImg.save(conf["files"]["resultfolder"] + "/" + conf["files"]["colors"])
    print("Generated Color Palette: ✔")
    return barColors
