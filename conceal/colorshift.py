from PIL import ImagePalette, Image


def colorshift(image_palette, image_to_quant):
    img = image_to_quant
    # color_palette = Image.open(image_palette)
    im = Image.open(img)
    conv = im.convert("P")
    conv.putpalette(image_palette)
    conv.save("results/quant1.png")
