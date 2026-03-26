import matplotlib.pyplot as plt
import numpy as np
overs = np.arange(1, 21)   
scores = [4,4,5,3,7,2,10,3,7,8,9,2,4,8,9,10,11,4,6,3]

plt.title("India's score over 20 overs (Bar chart)")
plt.xlabel("Over number")     
plt.ylabel("Runs scored")     

plt.bar(overs, scores)       
plt.xticks(overs)

plt.grid(axis='y', linestyle="--", alpha=0.9)

plt.show()