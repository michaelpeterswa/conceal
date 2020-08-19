import numpy as np
from PIL import Image
from opensimplex import OpenSimplex
from noise import snoise2


def generateRandomNoise(w, h):

    num_samples = w * h
    num_bins = 255

    # for pix in num_samples:
    return np.random.random(size=num_samples)


def generateSimplexNoise(w, h):

    num_samples = w * h

    arr = []
    simp = OpenSimplex()

    for y in range(0, h):
        for x in range(0, w):
            arr.append(simp.noise2d(x / 40, y / 40))

    return arr


def generatePerlinNoise(w, h):

    num_samples = w * h

    octaves = 7
    freq = 50.0 * octaves

    arr = []

    for y in range(0, h):
        for x in range(0, w):
            arr.append(snoise2(x / freq, y / freq, octaves) * 127.0 + 128.0)

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
            ((arr1[a] * weight1) + (arr2[a] * weight2) + (arr3[a] * weight3)) / 3
        )
    h_samples = np.reshape(np.asarray(final_values), (w, h))
    s_samples = np.reshape(arr1, (w, h))
    v_samples = np.reshape(arr1, (w, h))

    hsv_img = np.dstack([h_samples, s_samples, v_samples])

    image = Image.fromarray(np.uint8(hsv_img * 255), mode="HSV").convert("RGB")
    image.convert(mode="RGB", colors=16)
    image.save("results/noise.png")
