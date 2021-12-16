# -*- coding: utf-8 -*-
# https://www.w3schools.com/python/matplotlib_histograms.asp

import matplotlib.pyplot as plt
import numpy as np

# Matplotlib Histograms
# Create an array od, do, kolikPrvku
x = np.random.normal(0, 100, 25000)
plt.hist(x)
plt.title("Matplotlib Histograms")
plt.show()

# Matplotlib Pie Charts
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels=mylabels)
plt.legend(title="Four Fruits:")
plt.title("Matplotlib Pie Charts")
plt.show()
