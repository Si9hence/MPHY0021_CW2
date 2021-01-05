from rocksamples import *

def comparesamples(path_data1, path_data2, w_path = 'weights.csv', analysis='x', summary='criticality'):
    f_path = [path_data1, path_data2]
    w_path = 'weights.csv'
    w = load_weight(w_path)
    data = load_file(f_path)
    res = analyse(input_data=data, weight_data=w, analysis=analysis, summary=summary)
    return res