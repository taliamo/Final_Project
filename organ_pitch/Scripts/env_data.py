#T. Martz-Oberlander, 2015-11-15
#Upload and clean environmental data
# To run this script: $ python Scripts/env_data.py Data/[input filename] Figures/[output plot name] 


#Import useful libraries
import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np


#Define input arguments
input_file = sys.argv[1]
pitch_input = sys.argv[2]
output_plot_name = sys.argv[3]

#define variables for the Cramer pitch calculation
a0 = 331.5024
a9 = -(-85.20931)
a14 = 29.179762


