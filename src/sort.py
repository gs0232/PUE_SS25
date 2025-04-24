import numpy as np

def bubble_sort(given_array):
    n = len(given_array)
    for i in range(n):
        for j in range(0, n-i-1):
            if given_array[j] > given_array[j+1]:
                given_array[j], given_array[j+1] = given_array[j+1], given_array[j]
    return given_array