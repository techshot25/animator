#!/usr/bin/env python3

import numpy as np

def time_series(f, x_bounds=(0, 1), t_bounds=(0, 10), x_step=0.1, t_step=1):
    assert x_step > 0, f"x_step must be greater than zero, you entered {x_step}"
    assert t_step > 0, f"t_step must be greater than zero, you entered {t_step}"
    assert len(x_bounds) == 2, "x_bounds must be a (min, max) tuple or list."
    assert len(t_bounds) == 2, "t_bounds must be a (min, max) tuple or list."
    x = np.arange(start=x_bounds[0], end=x_bounds[1], step=x_step)
    t = np.arange(start=t_bounds[0], end=t_bounds[1], step=t_step)
    return np.array([f(x, ti) for ti in t])

#%%
import numpy as np
from numba import jit

@jit
def f(x, t):
    x = np.asarray(x)
    t = np.asarray(t)
    return np.array([np.sin(x - ti) for ti in t])

f([1,2,3], list(range(10000)))

#%%