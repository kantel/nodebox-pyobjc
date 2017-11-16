"""
======================
Frontpage plot example
======================

This example reproduces the frontpage simple plot example.
"""

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np

# nodebox section
if __name__ == '__builtin__':
    # were in nodebox
    import os
    import tempfile
    W = 800
    inset = 20
    size(W, 600)
    plt.cla()
    plt.clf()
    plt.close('all')
    def tempimage():
        fob = tempfile.NamedTemporaryFile(mode='w+b', suffix='.png', delete=False)
        fname = fob.name
        fob.close()
        return fname
    imgx = 20
    imgy = 0
    def pltshow(plt, dpi=150):
        global imgx, imgy
        temppath = tempimage()
        plt.savefig(temppath, dpi=dpi)
        dx,dy = imagesize(temppath)
        w = min(W,dx)
        image(temppath,imgx,imgy,width=w)
        imgy = imgy + dy + 20
        os.remove(temppath)
        size(W, HEIGHT+dy+40)
else:
    def pltshow(mplpyplot):
        mplpyplot.show()
# nodebox section end

with cbook.get_sample_data('membrane.dat') as datafile:
    x = np.fromfile(datafile, np.float32)
# 0.0005 is the sample interval

fig, ax = plt.subplots()
ax.plot(x, linewidth=4)
ax.set_xlim(5000, 6000)
ax.set_ylim(-0.6, 0.1)
ax.set_xticks([])
ax.set_yticks([])
#fig.savefig("membrane_frontpage.png", dpi=25)  # results in 160x120 px image
pltshow(plt)
