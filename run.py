import conceal

conf = conceal.config("conceal.toml")
conceal.normall(conf, "img_set1_wa")

conceal.collage(conf, "img_set1_wa_normalized", "results/collage0.png")

conceal.normone(conf, "results/collage0.png", "results/collage0.png")

colors1 = conceal.palette(conf, "results/collage0.png", "results/collage0_colors.png")
# colors2 = conceal.palette("results/collage1.png", "results/collage1colors.png")
w = conf["noise"]["width"]
h = conf["noise"]["height"]

conceal.gni(
    w,
    h,
    conceal.genrnoise(conf, w, h),
    conf["noise"]["randomweight"],
    conceal.gensnoise(conf, w, h),
    conf["noise"]["simplexweight"],
    conceal.genpnoise(conf, w, h),
    conf["noise"]["perlinweight"],
)

conceal.colshft(conf, colors1, "results/noise.png", "results/colorshift.png")
conceal.dith(conf, "results/colorshift.png", "results/dither.png")

conceal.voronoi(conf, "results/dither.png")

