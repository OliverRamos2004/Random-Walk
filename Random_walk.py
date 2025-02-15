import numpy as np
import matplotlib.pyplot as plt
import statistics as stats

walk_list = [np.array([0,0])] 
for i in range(1000):
    step=np.random.randn(2)
    walk_list.append(walk_list[-1]+step)
 
walk_array=np.array(walk_list)
x=walk_array[:,0]
y=walk_array[:,1]



def stepsize(walk_array):
    stepdist = np.diff(walk_array, axis=0)
    dx = stepdist[:,0]
    dy = stepdist[:,1]
    stepsize = np.sqrt(dx**2 + dy**2)
    return stepsize

def distance(walk_array):
    x = walk_array[:,0]
    y = walk_array[:,1]
    distance = np.sqrt(x**2 + y**2)
    return distance

stepsizes = stepsize(walk_array)
distances = distance(walk_array)

#-------- Plotting the data ----------------

fig1, axs = plt.subplots(2,2)
fig1.suptitle('Random Walk visualizations', fontsize=16, font='serif')

# Graph 1
axs[0,0].plot(x,y, 'tab:green')
axs[0,0].set_title('Plot visualization 2D', font='serif')
axs[0,0].set_xlabel('x')
axs[0,0].set_ylabel('y')
axs[0,0].grid(True)

# Graph 2
axs[1,0].plot(range(len(distances)), distances, 'tab:red')
axs[1,0].set_title('Distance from origin', font='serif')
axs[1,0].grid(True)
axs[1,0].set_xlabel('Step')
axs[1,0].set_ylabel('Distance from origin')

#Graph 3
axs[1,1].hist(stepsizes, bins=30, color='tab:blue')
axs[1,1].set_title('Histogram of x', font='serif')
axs[1,1].grid(True)
axs[1,1].set_xlabel('Size of step')
axs[1,1].set_ylabel('Frequency')

axs[0,1].axis('off')

plt.show()