#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def get_data(data_file_name):
    try:
        data_file = open(data_file_name)
    except:
        print("Błąd, zła nazwa pliku")
        sys.exit(0)

    vector_x = []
    vector_y = []
    try:
        for line in data_file.readlines():
            line = line.split()
            vector_x.append(float(line[0]))
            vector_y.append(float(line[1]))

        return vector_x, vector_y
    except:
        print("Zły format pliku z danymi")
        sys.exit(0)

def get_average(vector):
    avg = sum(vector) / len(vector)

    return avg


def get_product(vector1, vector2):
    product = []

    for x in range(len(vector1)):
        product.append(vector1[x] * vector2[x])

    return product


def get_trendline(data):
    vector_x = data[0]
    vector_y = data[1]
    xy_vector = get_product(vector_x, vector_y)
    xx_vector = get_product(vector_x, vector_x)
    x_average = get_average(vector_x)
    y_average = get_average(vector_y)
    vector_length = len(vector_x)

    try:
        a = (sum(xy_vector) - (vector_length * x_average * y_average)) / (
            sum(xx_vector) - vector_length * x_average ** 2)
        b = y_average - (a * x_average)

        print("{:.3f}\n{:.3f}".format(a, b))
    except:
        print("Dla tych danych nie można wyznaczyć linii trendu")


get_trendline(get_data(sys.argv[1]))
