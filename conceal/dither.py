from PIL import Image


def dither(conf, image, save):
    im = Image.open(image)
    im = im.quantize(colors=conf["finalcolors"]["amount"])
    im.save(save)
