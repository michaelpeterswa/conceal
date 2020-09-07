import conceal


def run(conf):
    print("Starting Up Conceal: ✔")
    conceal.normall(conf)
    conceal.collage(conf)
    conceal.normone(conf)
    conceal.gni(conf)
    conceal.colshft(conf, conceal.palette(conf))
    conceal.dith(conf)
    conceal.voronoi(conf)
    print("Camouflage Generation Complete: ✔")
