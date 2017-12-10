import numpy as np

data = np.genfromtxt("content/blei.txt", unpack=True)
print(data)
kap = (data[0]*4.18+338.96)*(data[3] - data[2])/((683.39-140.05)*(data[1]-data[3]))

file = open("content/b.txt", "w")
for i in range(len(kap)):
    file.write(str(kap[i]) + "\n")
