import matplotlib.pyplot as plt
import matplotlib.axes as axes
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd

time = pd.read_csv('time.csv')
memory = pd.read_csv('memory.csv')

time.plot(x='n', kind='line', title= 'Runtime', ylabel='Time (s)', grid=True)
memory.plot(x='n', kind='line', title= 'Memory Usage', ylabel='Memory (bytes)', grid=True).ticklabel_format(style='plain')
plt.show()