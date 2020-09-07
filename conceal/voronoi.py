# adapted from https://rosettacode.org/wiki/Voronoi_diagram#Python

from PIL import Image
import random
import math
from tqdm import tqdm


def genvoronoi(conf):

    height = conf["noise"]["height"]
    width = conf["noise"]["width"]
    num_cells = conf["voronoi"]["cells"]

    baseimg = Image.open(conf["files"]["resultfolder"] + "/" + conf["files"]["dither"])
    rgbbase = baseimg.convert("RGB")
    image = Image.new("RGB", (width, height))
    putpixel = image.putpixel
    imgx, imgy = image.size
    nx = []
    ny = []
    nr = []
    ng = []
    nb = []
    for i in tqdm(range(num_cells), desc="Creating Points"):
        nx.append(random.randrange(1, imgx))
        ny.append(random.randrange(1, imgy))
        rgb = rgbbase.getpixel((nx[i], ny[i]))
        nr.append(rgb[0])
        ng.append(rgb[1])
        nb.append(rgb[2])
    for y in tqdm(range(imgy), desc="Tessellating"):
        for x in range(imgx):
            dmin = math.hypot(imgx - 1, imgy - 1)
            j = -1
            for i in range(num_cells):
                d = math.hypot(nx[i] - x, ny[i] - y)
                if d < dmin:
                    dmin = d
                    j = i
            putpixel((x, y), (nr[j], ng[j], nb[j]))
    print("Tessellated Camouflage Pattern: ✔")
    image.save(conf["files"]["resultfolder"] + "/" + conf["files"]["output"], "PNG")

