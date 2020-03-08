import math
import numpy as np
import matplotlib.pyplot as plt 

dataset = open(r'./datasets/swedish_car_insurance.txt', 'r')
lines = dataset.readlines()
lines = list(filter(lambda line: not not line, lines))
X, Y = [], []
for line in lines:
    parts = line.split()
    X.append(float(parts[0].replace(',','.')))
    Y.append(float(parts[1].replace(',','.')))
dataset.close()


def estimate_coeff(X, Y):
    n = len(X)
    m_X = np.mean(X)
    m_Y = np.mean(Y)

    SS_xy = np.sum(X*Y) - n*m_X*m_Y
    SS_xx = np.sum(X*X) - n*m_X*m_X

    b1 = SS_xy / SS_xx
    b0 = m_Y - b1 * m_X

    return(b0, b1)

def plot_regression_line(x, y, b):
    plt.scatter(x, y, color = "m",
    marker = "o", s = 30)
    y_pred = b[0] + b[1]*x
    plt.plot(x, y_pred, color = "g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

x = np.array(X)
y = np.array(Y)
b = estimate_coeff(x, y)
plot_regression_line(x, y, b)

def getCost(X, Y, b0, b1):
    cost = 0
    for idx in range(len(X)):
        cost += math.pow((b0 + b1 * X[idx]) - Y[idx], 2)
    cost  = cost / (2 * len(X))
    return cost

minB0, minB1 = -100, -100
minError = getCost(X, Y, minB0, minB1)
for b0 in range(-99, 101):
    for b1 in range(-99, 101):
        currentCost = getCost(X, Y, b0, b1)
        if minError > currentCost:
            minError = currentCost
            minB0 = b0
            minB1 = b1

for idx in range(len(X)):
    print('X: ',  X[idx], 'Y: ', Y[idx], 'Predicted: ', b[0]  + b[1] * X[idx], 'Poor predict:', minB0 + minB1 * X[idx])
plot_regression_line(x, y, [minB0, minB1])

print('Math: ', b[0], ', ', b[1], '. ', minB0, ', ', minB1)
