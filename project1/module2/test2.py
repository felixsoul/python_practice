import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
print(parent_dir)
sys.path.append(parent_dir)
from my_package import my_function
my_function()