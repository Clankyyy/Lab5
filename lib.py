import numpy as np
import matplotlib.pyplot as plt

import matplotlib.dates

from datetime import datetime, timedelta


def display():
    show_function()
    #show_temperature()
    #show_sales()
    #show_weight_cor()
    #show_marks()


def show_temperature():
    measures = [-7, -7, -6, -5, -7, -6, -9, -5]
    time = [datetime(2023, 11, 30, 6) + timedelta(hours=i) for i in range(8)]

    fig, ax = plt.subplots()
    myFmt = matplotlib.dates.DateFormatter("%H:%M")
    ax.xaxis.set_major_formatter(myFmt)

    ax.set(xlabel="Time ", ylabel="Temperature", title="Mesures")
    ax.grid()

    ax.plot(time, measures)

    plt.gcf().autofmt_xdate()
    plt.show()


def show_sales():
    np.random.seed(123)

    categories = ["Milk", "Bread", "Meat", "Ice Cream", "Sugar"]
    sales = np.random.randint(300, 1000, len(categories))

    fig, ax = plt.subplots()

    ax.set(xlabel="Categories ", ylabel="Sales(count)", title="Sales per day")

    plt.bar(categories, sales)
    plt.show()


def show_weight_cor():
    height = np.linspace(140, 200, 10)
    weight = [42, 43, 47, 54, 60, 64, 70, 73, 76, 83]

    plt.title("Correlation between height and weight")
    plt.xlabel("Height")
    plt.ylabel("Weight")

    plt.scatter(height, weight)
    plt.show()


def show_marks():
    y = np.random.randint(1, 6, 120)

    plt.title("Distribution of grades of students from 5 groups")
    plt.xlabel("Mark")
    plt.ylabel("Number of students")

    plt.hist(y, 5)
    plt.xticks(np.arange(1, 6, step=1))
    plt.show()


def show_function():
    plt.suptitle("2d function")
    x = np.arange(-20, 20, 0.2)
    y = np.arange(-20, 20, 0.2)

    xv, yv = np.meshgrid(x, y, sparse=True)
    z = np.tan(xv*2 / yv*2)
    h = plt.contour(x, y, z) 

    plt.show()


if __name__ == "__main__":
    display()
