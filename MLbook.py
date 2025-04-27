# import matplotlib.pyplot as plt
import math

def mean(sampleset):
    total = 0
    for ele in sampleset:
        total = total + ele
    return total/len(sampleset)

def variance(sampleset):
    total = 0
    samplemean = mean(sampleset)
    for ele in sampleset:
        total = total + (math.pow(ele-samplemean, 2))

    return total/len(sampleset)

myset1 = [2., 10., 3., 6., 4., 6., 10.]
myset2 = [1., -100., 15., -100., 21.]
# print("Variance of first set:" + str(variance(myset1)))
# print("Variance of second set:" + str(variance(myset2)))

# bernoulli distribution
import numpy as np
import matplotlib.pyplot as plt
plt.figure()
distro = np.random.binomial(1, .6, 10000)/0.5
plt.hist(distro, 2 , density=True)