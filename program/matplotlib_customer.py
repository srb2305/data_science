import numpy as np
import matplotlib.pyplot as plt


#Average customer arrivals per hour
avg_arrivals = 10

#standard devoation of arrivals
std_dev = 2

#Number of hours
hours = 24

#generate customer arrivals
arrivals = avg_arrivals + std_dev * np.random.randn(hours)  

#Ensure arrivals are non-negative
arrivals = np.maximum(arrivals, 0)  

#Plot customer arrivals 
plt.plot(arrivals)
plt.title('simulated cusomer arrivals')
plt.xlabel('Hour')
plt.ylabel('Arrivals')
plt.show()