import conceal

w = 500
h = 500

conceal.normall("img_set1_wa")

conceal.collage("img_set1_wa_normalized", "results/collage0.png")

conceal.normone("results/collage0.png", "results/collage0.png")

colors1 = conceal.palette("results/collage0.png", "results/collage0_colors.png")

conceal.gni(
    w,
    h,
    conceal.genrnoise(w, h),
    0.60,
    conceal.gensnoise(w, h),
    0.30,
    conceal.genpnoise(w, h),
    0.10,
)

conceal.colshft(colors1, "results/noise.png")
conceal.dith("results/quant1.png", "results/dith1.png")

conceal.voronoi(500, 500, 1000, "results/quant2.png")

