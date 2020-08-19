# adapted from https://rosettacode.org/wiki/Voronoi_diagram#Python

from PIL import Image
import random
import math


def genvoronoi(width, height, num_cells, image):

    baseimg = Image.open(image)
    rgbbase = baseimg.convert("RGB")
    image = Image.new("RGB", (width, height))
    putpixel = image.putpixel
    imgx, imgy = image.size
    nx = []
    ny = []
    nr = []
    ng = []
    nb = []
    for i in range(num_cells):
        nx.append(random.randrange(imgx))
        ny.append(random.randrange(imgy))
        rgb = rgbbase.getpixel((nx[i], ny[i]))
        nr.append(rgb[0])
        ng.append(rgb[1])
        nb.append(rgb[2])
    for y in range(imgy):
        for x in range(imgx):
            dmin = math.hypot(imgx - 1, imgy - 1)
            j = -1
            for i in range(num_cells):
                d = math.hypot(nx[i] - x, ny[i] - y)
                if d < dmin:
                    dmin = d
                    j = i
            putpixel((x, y), (nr[j], ng[j], nb[j]))
    image.save("results/voronoi.png", "PNG")

