#!/usr/bin/env python3
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt

class ScatterAnimation:
    def __init__(self, x, Y, interval=500, margin_percentage=0.05, c=None, s=None):
        """
        Parameters
        ----------
        x : array-like
            A 1D array defining the range values.
        Y : array-like
            A list of arrays each of size (t, y) where t is time intervals
            and y is the range of x which must be the same size x.
        """
        self.x = np.asarray(x).flatten()
        self.Y = np.asarray(Y)
        assert self.Y.shape[-1] == self.x.shape[0], "Last dimension in Y must equal the dimension x"
        self.fig, self.ax = plt.subplots()
        self.c = c
        self.s = s
        self.p = margin_percentage
        self.anim = FuncAnimation(self.fig, self.update, interval=interval, 
                                  frames=self.Y.shape[0],
                                  init_func=self.init_func, blit=True);

    def init_func(self):
        x = self.x
        y = self.Y[0]
        c = self.c[0] if isinstance(self.c, (list, tuple, np.ndarray)) else self.c
        s = self.s[0] if isinstance(self.s, (list, tuple, np.ndarray)) else self.s
        self.scat = self.ax.scatter(x, y, c=c, s=s)
        self.ax.axis([
            x.min() - self.p * np.ptp(x), # xmin
            x.max() + self.p * np.ptp(x), # xmax
            self.Y.min() - self.p * np.ptp(self.Y), # ymin
            self.Y.max() + self.p * np.ptp(self.Y) # ymax
        ])
        return self.scat,
    
    def update(self, i):
        y = self.Y[i]
        self.scat.set_offsets(np.c_[self.x, y])
        if self.s is not None:
            self.scat.set_sizes(self.s[i] if isinstance(self.s, (list, tuple, np.ndarray)) else self.s)
        if self.c is not None:
            self.scat.set_array(self.c[i] if isinstance(self.c, (list, tuple, np.ndarray)) else self.c)
        return self.scat,
