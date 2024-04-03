import numpy as np

def calculate(input_list): 
    if not len(input_list) == 9:
        raise ValueError("List must contain nine numbers.")

    funcs = {   
        'mean': lambda x: np.mean(x), 
        'variance': lambda x: np.var(x), 
        'standard deviation': lambda x: np.std(x),
        'max': lambda x: np.max(x), 
        'min': lambda x: np.min(x),
        'sum': lambda x: np.sum(x)
    }
    
    a = np.array(input_list).reshape(3,3)

    calculations = { 
        k:[[v(c) for c in a.T], [v(r) for r in a], v(a)] for k,v in funcs.items()
    }
    
    return calculations





#print(calculate(test) == solution)