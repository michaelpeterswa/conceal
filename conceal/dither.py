from PIL import Image


def dither(conf):
    im = Image.open(conf["files"]["resultfolder"] + "/" + conf["files"]["colorshift"])
    im = im.quantize(colors=conf["colors"]["dither"])
    im.save(conf["files"]["resultfolder"] + "/" + conf["files"]["dither"])
    print("Dithered Image: ✔")
