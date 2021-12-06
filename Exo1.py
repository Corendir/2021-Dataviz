import numpy as np
import matplotlib.pyplot as plt

def subplot(index, title):    
    # To be completed
    return ax

fig = plt.figure(figsize=(13,5), dpi=300)
X = np.linspace (-4,4,200)

subplot(1, "y = cos(x)").plot(X, np.cos(X), "C1")
subplot(2, "y = sin(x)").plot(X, np.sin(X), "C1")
subplot(3, "y = tan(x)").plot(X, np.tan(X), "C1")
subplot(4, "y = cosh(x)").plot(X, np.cosh(X), "C1")
subplot(5, "y = sinh(x)").plot(X, np.sinh(X), "C1")
subplot(6, "y = tanh(x)").plot(X, np.tanh(X), "C1")

plt.show()