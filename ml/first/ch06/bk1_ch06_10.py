import random
import statistics
import matplotlib.pyplot as plt

num_flips = 1000

results = [random.choices([0,1],[0.4, 0.6])[0] 
           for _ in range(num_flips)]

running_means = [statistics.mean(results[0:idx+1]) 
                 for idx in range(num_flips)]

visual_num = 100
plt.scatter(range(1,visual_num+1), results[0:visual_num],
            c = results[0:visual_num], marker="o", cmap="cool")
plt.plot(range(1, visual_num+1), results[0:visual_num])
plt.xlabel("Number of coin flips")
plt.ylabel("Result")
plt.grid(True)
plt.show()

plt.plot(range(1, num_flips+1), running_means)
plt.axhline(0.5, color = 'r')
plt.xlabel("Number of coin flips")
plt.ylabel('Running Mean')
plt.grid(True)
plt.ylim(0,1)
plt.show()