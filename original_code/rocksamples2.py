from math import *
import numpy as np
import yaml
from argparse import ArgumentParser

def analyse(input_data, weight_data, analysis='x', summary='criticality'):
    # we set cri as 5 this could be modify later
    cri = 5

    if analysis == "x":
        d = analysis_x(input_data, weight_data)
    elif analysis == "y":
        d = analysis_y(input_data, weight_data)
    
    if summary == "criticality":
        res = summary_cri(input_data=d, cri=cri)
    elif summary == "d":
        res = summary_d(input_data=d)

    return res

def analysis_x(input_data, weight_data):
    res = weight_data * np.abs(input_data[0] - input_data[1])
    # nansum here used to ignore nan input
    res = np.nansum(res, axis=1)
    return res

def analysis_y(input_data, weight_data):
    res = weight_data * (input_data[0] - input_data[1])**2
    res = np.nansum(res, axis=1)
    res = np.sqrt(res)
    return res

def summary_cri(input_data, cri=5):
    res = np.sum(input_data > cri)
    print("criticality:", res, "results above 5")
    return res

def summary_d(input_data):
    res = np.average(input_data)
    print("d-index:", res)
    return  res

def load_file(path):
    res = []
    for p in path:
        with open(p) as f:
            lines = f.readlines()
            data = []
            for line in lines:
                row = []
                for n in line.split(','):
                    row.append(float(n.strip()))
                data.append(row)
        res.append(data)
    return np.asarray(res)

def load_weight(path):
    with open(path) as filew:
        linew = filew.read()
        w = []
        for n in linew.split(','):
            w.append(float(n.strip()))
    return w

def process():

    parser = ArgumentParser(description="comparesamples <sample file 1> <sample file 2> \
        [--summary <measure>] \
        [--analysis <algorithm>] [--weights <weights file>]")
    parser.add_argument('--analysis', help="analysis input should be x or y", type=str)
    parser.add_argument('--summary', help="summary input should be either d or criticality", type=str)
    parser.add_argument('--weights', help="file path of weights", type=str)
    parser.add_argument('file1', help="file path of data1")
    parser.add_argument('file2', help="file path of data2")
    arguments= parser.parse_args()
    
    print([arguments.file1, arguments.file2])
    message = analyse(input_data=[arguments.file1, arguments.file2], weight_data=arguments.weights,
                    analysis=arguments.analysis, summary=arguments.summary)
    print(message)

def YAML(path):
    with open(path) as yaml_file:
        my_data = yaml.safe_load(yaml_file)
    print(my_data)


if __name__ == "__main__":


    parser = ArgumentParser(description="comparesamples <sample file 1> <sample file 2> \
    [--summary <measure>] \
    [--analysis <algorithm>] [--weights <weights file>]")
    parser.add_argument('--config',  help= "YAML input", type =str)
    parser.add_argument('--analysis',  help="analysis input should be x or y", type=str)
    parser.add_argument('--summary', help="summary input should be either d or criticality", type=str)
    parser.add_argument('--weights',  help="file path of weights", type=str)
    parser.add_argument('--file1', nargs='+', help="file path of data1")
    parser.add_argument('--file2', nargs='+', help="file path of data2")
    arguments= parser.parse_args()

    #a = load_file(arguments.file1)
    #print(a)
    #process()
    
    YAML('my_config.yaml')

    


'''
    with open(arguments.file1) as file1:
        lines1 = file1.readlines()
        data1 = []
        for line in lines1:
            row = []
            for n in line.split(','):
                row.append(float(n.strip()))
            data1.append(row)
        print(data1)
'''