import math
import numpy as np
import matplotlib.pyplot as plt
from FastICA import ICA


def mix(wave1, wave2, ratio=0.5):
    try:
        print(type(wave1))
        new_wave = wave1 * ratio + wave2 * (1 - ratio)
        return new_wave
    except:
        print("Both waves should be a same length.")


# original waves
wave1 = np.array([math.sin(i/45) for i in range(1000)])
wave2 = np.array([1 if (i // 50) % 2 == 0 else -1 for i in range(1000)])
fig = plt.figure()
ax1 = fig.add_subplot(311)
ax1.set_title("Original Waves")
ax1.plot(wave1)
ax1.plot(wave2)

# mixed waves
new_wave1 = mix(wave1, wave2, ratio=0.5)
new_wave2 = mix(wave1, wave2, ratio=0.8)
ax2 = fig.add_subplot(312)
ax2.set_title("Mixed Waves")
ax2.plot(new_wave1)
ax2.plot(new_wave2)

# restore waves
X = np.vstack((new_wave1, new_wave2))
restored_X = ICA(X)
ax3 = fig.add_subplot(313)
ax3.set_title("Restored Waves")
ax3.plot(restored_X[0])
ax3.plot(restored_X[1])
fig.show()