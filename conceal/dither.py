from PIL import Image


def dither(image, save):
    im = Image.open(image)
    im = im.quantize(colors=4, kmeans=100)
    im.save("results/quant2.png")
