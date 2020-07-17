# Animator

A python tool for making animated plots

## Dependencies

matplotlib>=3.1.3
numpy>=1.18.1

## Example usage

```python
from animator import ScatterAnimation
from matplotlib.animation import PillowWriter

x = np.linspace(0, 10, 100)
Y = [np.sin(x - 0.01 * t) for t in range(10)]
animation = ScatterAnimation(x, Y)
writer = PillowWriter(fps=5)
animation.anim.save("sin_wave.gif", writer=writer)
```

Which writers the `sin_wave.gif` in the current work directory

## To Do

- Implement line plot
- Implement ffmpeg saving
- Remove initial plot lines
- Add test cases