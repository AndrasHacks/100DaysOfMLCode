import math

dataset = open(r'./datasets/swedish_car_insurance.txt', 'r')
lines = dataset.readlines()
lines = list(filter(lambda line: not not line, lines))
X, Y = [], []
for line in lines:
    parts = line.split()
    X.append(float(parts[0].replace(',','.')))
    Y.append(float(parts[1].replace(',','.')))
dataset.close()

minB0, minB1 = -1000, -1000

def getCost(X, Y, b0, b1):
    cost = 0
    for idx in range(len(X)):
        cost += (b0 + b1 * X[idx]) - Y[idx]
    cost = math.pow(cost, 2) / 2 * len(X)
    return cost

minError = getCost(X, Y, -100, -100)
for b0 in range(-99, 101):
    for b1 in range(-99, 101):
        currCost = getCost(X, Y, b0, b1)
        if currCost < minError:
            minB0 = b0
            minB1 = b1
            minError = currCost

print('B0: ', minB0, ' B1: ', minB1, 'minError: ', minError)

# for idx in range(len(X)):
#    print('X: ',  X[idx], 'Y: ', Y[idx], 'Predicted: ', minB0 + minB1 * X[idx])
