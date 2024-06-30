import scipy
print("scip: %s" % scipy.__version__)

import numpy
print("numpy: %s" % numpy.__version__)

import numpy as np

x_array = np.arange(10)
print(x_array)

def my_function(x,y):

    """
    这个自定义函数计算两个数值x和y的和
    """
    return x+y

print(my_function(5,2))