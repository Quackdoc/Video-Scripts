# Import matplotlib and numpy libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('lum-mod.csv')

fig, ax = plt.subplots()

df.plot(x="frame", y="avg" , ax=ax)
df.plot(x="frame", y="95th", ax=ax)
df.plot(x="frame", y="99th", ax=ax)



# Set the title and labels for the axes object
ax.set_title("Video nits over time")
ax.set_xlabel("Time")
ax.set_ylabel("Luminance cd/m^2")

# Add a legend to show the labels of each line
ax.legend()

# Show the figure
plt.yscale("log")
plt.ylim(0.1,10001)
plt.axhline(y=1, linestyle=":")
plt.axhline(y=100, linestyle=":")

plt.show()