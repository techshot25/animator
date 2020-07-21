#from unittest import TestCase
from animator.plotter import ScatterAnimation
from matplotlib.animation import PillowWriter
import numpy as np
x = np.linspace(0, 10, 100)
Y = [np.sin(x - 0.1 * t) for t in range(10)]
animation = ScatterAnimation(x, Y)
writer = PillowWriter(fps=5)
animation.anim.save("test.gif", writer=writer)
