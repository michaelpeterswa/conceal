import numpy as np
from PIL import Image
from opensimplex import OpenSimplex
from noise import snoise2


def generateRandomNoise(conf, w, h):

    num_samples = w * h
    num_bins = 255

    # for pix in num_samples:
    return np.random.random(size=num_samples)


def generateSimplexNoise(conf, w, h):

    num_samples = w * h

    arr = []
    simp = OpenSimplex()

    for y in range(0, h):
        for x in range(0, w):
            arr.append(simp.noise2d(x / 40, y / 40))

    return arr


def generatePerlinNoise(conf, w, h):

    num_samples = w * h

    octaves = conf["perlin"]["octaves"]
    freq = conf["perlin"]["frequency"] * octaves

    arr = []

    for y in range(0, h):
        for x in range(0, w):
            arr.append(snoise2(x / freq, y / freq, octaves))

    return arr


def generateNoiseImage(w, h, arr1, weight1, arr2, weight2, arr3, weight3):

    num_samples = w * h
    final_values = []

    static_val = np.empty(num_samples)
    static_val.fill(0.5)

    static_val2 = np.empty(num_samples)
    static_val2.fill(1.0)

    for a in range(0, w * h):
        final_values.append(
            (
                (arr1[a] * weight1)
                + (((arr2[a] / 2) + 0.5) * weight2)
                + (((arr3[a] / 2) + 0.5) * weight3)
            )
            / 3
        )

    h_samples = np.reshape(np.asarray(final_values), (w, h))
    s_samples = np.reshape(static_val, (w, h))
    v_samples = np.reshape(static_val2, (w, h))

    hsv_img = np.dstack([h_samples, s_samples, v_samples])

    image = Image.fromarray(np.uint8(hsv_img * 255), mode="HSV").convert("RGB")
    image = image.quantize(colors=6)
    image.convert(mode="RGB")
    image.save("results/noise.png")
