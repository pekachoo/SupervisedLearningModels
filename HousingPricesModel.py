import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# linear regression model with square cost function and gradiant descent
# https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction

# define functions
def cost_function(slope, intercept, size, x_points, y_points):
    # function of slope
    total_cost = 0
    for i in range(size):
        f_wb = slope * x_points[i] + intercept
        y_i = y_points[i]
        total_cost += ((f_wb - y_i) ** 2)
    return total_cost / (2 * size)


def calculate_derivatives(x_points, y_points, slope, intercept):
    # batch gradient descent
    size = x_points.shape[0]
    dJ_dw = 0
    dJ_db = 0

    for i in range(size):
        x_i = x_points[i]
        y_i = y_points[i]
        f_wb = slope * x_points[i] + intercept
        temp_dJ_dw = (f_wb - y_i) * x_i
        temp_dJ_db = (f_wb - y_i)
        dJ_dw += temp_dJ_dw
        dJ_db += temp_dJ_db
    dJ_dw = dJ_dw / size
    dJ_db = dJ_db / size
    return dJ_dw, dJ_db


def gradiant_descent(x_points, y_points, slope_i, intercept_i, l_rate, num_iterations):
    cost_arr = [cost_function(slope_i, intercept_i, x_points.shape[0], x_points, y_points)]
    slope_arr = [slope_i]

    slope = slope_i
    intercept = intercept_i

    for i in range(num_iterations):
        dJ_dw, dJ_db = calculate_derivatives(x_points, y_points, slope_i, intercept_i)
        slope = slope - l_rate * dJ_dw
        intercept = intercept - l_rate * dJ_db

        cost_arr.append(cost_function(slope, intercept, x_points.shape[0], x_points, y_points))
        slope_arr.append(slope)
    return cost_arr, slope_arr, slope, intercept


# read file data

data = pd.read_csv('Housing.csv')

areas = np.array(data['area'])
prices = np.array(data['price'])

plt.plot(areas, prices, 'o')
# plt.xlim(0, 12000)
plt.show()
