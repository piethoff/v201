#Use:
#python var.py [data].txt [column]
#

import numpy as np
import sys

def mean(a):
    sum = 0
    for i in a:
        sum += i
    sum = sum/len(a)
    return sum

def var(a):
    mean2 = mean(a)
    sum = 0
    for i in a:
        sum += (i-mean2)**2
    sum = sum/len(a)
    sum = sum/(len(a) - 1)
    return np.sqrt(sum)

#data = np.genfromtxt(str(sys.argv[1]), unpack=True)
#if(data.ndim == 2):
#    data = data[int(sys.argv[2])]
#print(data)
#print(mean(data), "+/-", var(data), sep="")

data = np.genfromtxt("content/kupfer.txt", unpack=True)
kap = (data[0]*4.18+338.96)*(data[3] - data[2])/((378.36-140.05)*(data[1]-data[3]))

print("Wärmekapazität: \t", mean(kap), "+/-", var(kap), sep="")
print("Tk: \t\t\t" , mean(data[1]), "+/-", var(data[1]), sep="")

data = np.genfromtxt("content/alu.txt", unpack=True)
kap = (data[0]*4.18+338.96)*(data[3] - data[2])/((254.49-140.05)*(data[1]-data[3]))

print("Wärmekapazität: \t", mean(kap), "+/-", var(kap), sep="")
print("Tk: \t\t\t" , mean(data[1]), "+/-", var(data[1]), sep="")

data = np.genfromtxt("content/blei.txt", unpack=True)
kap = (data[0]*4.18+338.96)*(data[3] - data[2])/((683.39-140.05)*(data[1]-data[3]))

print("Wärmekapazität: \t", mean(kap), "+/-", var(kap), sep="")
print("Tk: \t\t\t" , mean(data[1]+273.15), "+/-", var(data[1]+273.15), sep="")