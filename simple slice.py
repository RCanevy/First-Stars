# -*- coding: utf-8 -*-
"""
Simple Slice

"""

import os
import yt


data_dir = '/disk12/brs/pop2-prime/firstpop2_L2-Seed3_large/pisn_solo/'
plot_directory = '/home/rcanevy/plots/slices'
sample_plot = 'AltSlice_DD0098.png'
path = os.path.join(data_dir, "DD0098", "DD0098")
ds = yt.load(path)
plt = yt.SlicePlot(ds, "z", ("gas", "density"), center=("max", "density"), width=(80.0, "kpc"))
plt.save(os.path.join(plot_directory, sample_plot))

