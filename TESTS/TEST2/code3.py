import pandas as pd
import numpy as np
def example_function():
    return pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])

def another_function(x):
    return np.sqrt(x)

def yet_another_function(lst):
    return [i * 2 for i in lst]