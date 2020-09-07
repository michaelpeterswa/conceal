from conceal import config
from conceal import normalize
from conceal import collage
from conceal import palette
from conceal import noise
from conceal import colorshift
from conceal import dither
from conceal import voronoi
from conceal import runner

runner = runner.run
config = config.configure
normall = normalize.normalize
normone = normalize.normalize_one
collage = collage.collage
palette = palette.generate
genrnoise = noise.generateRandomNoise
gensnoise = noise.generateSimplexNoise
genpnoise = noise.generatePerlinNoise
gni = noise.generateNoiseImage
colshft = colorshift.colorshift
dith = dither.dither
voronoi = voronoi.genvoronoi
