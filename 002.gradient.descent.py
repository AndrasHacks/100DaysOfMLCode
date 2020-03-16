# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np


def main():
    # y = mx + b
    # y = b0 + b1x
    
    dataset = open(r'./datasets/002.gradient.descent.csv', 'r')
    lines = dataset.readlines()
    lines = list(filter(lambda line: not not line, lines))
    dataset.close()
    X, Y = [], []
    
    for line in lines:
        measurements = line.split(',')
        X.append(float(measurements[0]))
        Y.append(float(measurements[1]))
        
    b0, b1 = gradient_descent_runner(X, Y, 0, 0, 0.0001, 1000)
    print ('B0: {0}, B1 = {1}'.format(b0, b1))
    plot_measurements(X, Y, b0, b1)
    
def computeCostForLineGivenWeights(b0, b1, x, y):
    totalCost = 0
    for ind in range(len(x)):
        totalCost += (y[ind] - (b0 + b1 * x[ind])) ** 2
    return totalCost / float(len(x))
    
def stepGradient(b0_current, b1_current, learning_rate, x, y):
    b0_gradient = 0
    b1_gradient = 0
    N = float(len(x))
    for i in range(len(x)):
        b0_gradient += -(2/N) * (y[i] - ((b1_current*x[i]) + b0_current))
        b1_gradient += -(2/N) * x[i] * (y[i] - ((b1_current * x[i]) + b0_current))
    new_b0 = b0_current - (learning_rate * b0_gradient)
    new_b1 = b1_current - (learning_rate * b1_gradient)
    return [new_b0, new_b1]

def gradient_descent_runner(x, y, start_b0, start_b1, learning_rate, iterations):
    b0 = start_b0
    b1 = start_b1
    
    for i in range(iterations):
        b0, b1 = stepGradient(b0, b1, learning_rate, x, y)
        
    return [b0, b1]
    
def plot_measurements(x, y, b0, b1):
    plt.scatter(x, y, color = 'b', marker = 'o', s = 30)
    plt.xlabel('x')
    plt.ylabel('y')
    x = np.array(X)
    y_pred = b0 + b1*x
    plt.plot(x, y_pred, color = "r")
    plt.show()

if __name__ == '__main__':
    main()
