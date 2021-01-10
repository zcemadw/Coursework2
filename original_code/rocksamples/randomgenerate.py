import csv
import numpy as np
f = open('Random.csv')
csv_f = csv.reader(f)

def generate_random_inputs(a,b):
    random_array = np.random.rand(3,2)
    return random_array
