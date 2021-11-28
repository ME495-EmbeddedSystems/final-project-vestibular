import threading
import time
import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def __init__(self):
      self.lock = threading.Lock()
      self.t_start = time.time()
      self.data = {}
      self.tstamp = {}


    def log(self, header, value):
      t = time.time() - self.t_start
      with self.lock:
        if header in self.data.keys():
          self.data[header].append(value)
          self.tstamp[header].append(t)
        else:
          self.data[header] = [value]
          self.tstamp[header] = [t] 
      
    def plot(self):
      fig, ax = plt.subplots()
      for header in self.data.keys():
        ax.plot(np.array(self.tstamp[header]), np.array(self.data[header]))
      ax.legend(self.data.keys())
      plt.show()

    def reset(self, msg):
      self.data = {}
      self.t_start = time.time()