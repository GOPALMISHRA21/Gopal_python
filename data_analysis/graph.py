import numpy as np
import matplotlib.pyplot as plt

rainfall = np.array([23,5,67,32,56,76])
years= np.array([2010,2011,2012,2013,2014,2015])

plt.bar(years,rainfall)
plt.show()

