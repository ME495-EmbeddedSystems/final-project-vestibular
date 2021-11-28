import threading
import time
import matplotlib.pyplot as plt
import numpy as np

class Plotter:

  class Line:
    def __init__(self):
      self.times = []
      self.data = []

  class Plot:
    def __init__(self):
      self.lines = {}

    def add(self, line, data, t):

      if not line in self.lines.keys():
        self.lines[line] = Plotter.Line()

      self.lines[line].times.append(t)
      self.lines[line].data.append(data)

  def __init__(self):
    self.t_start = time.time()
    self.plots = {}

  def log(self, plot, line, data):
    t = time.time() - self.t_start
    if not plot in self.plots.keys():
      self.plots[plot] = Plotter.Plot()
    self.plots[plot].add(line, data, t)

  def plot(self):
    for plot in self.plots.keys():
      fig, ax = plt.subplots()
      for line in self.plots[plot].lines.keys():
        ax.plot(
          np.array(self.plots[plot].lines[line].times),
          np.array(self.plots[plot].lines[line].data)
        )
      ax.legend(self.plots[plot].lines.keys())
      plt.title(plot)
    plt.show()

  def reset(self):
    self.plots = {}
    self.t_start = time.time()