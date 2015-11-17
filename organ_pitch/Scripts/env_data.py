#T. Martz-Oberlander, 2015-11-15
#Upload and clean environmental data
# To run this script: $ python Scripts/env_data.py Data/[input filename] Figures/[output plot name] 

#Import useful libraries
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

%matplotlib inline

#Define input arguments	
input_file = sys.argv[1]
output_plot_name = sys.argv[2]

#define variables for the Cramer pitch calculation
a0 = 331.5024
a9 = -(-85.20931)
a14 = 29.179762


#I open my main function
def main:

#Upload environmental data file
	env = pd.read_table(input_file, sep=',')

#assigning columns names
	env.columns=[['test', 'date_time','temp C', 'RH %', 'CO2_1', 'CO2_2']]	

#change data time variable to actual values of time. 
	env['date_time']= pd.to_datetime(env['date_time'])

#test function
def test_cramer():
    assert a0 + ((a9)*400)/100 + a14*((400/1000000)**2) == 672.339644669, 'Equation failure'
    return()

#Call the test function
test_cramer()
       
#pitch calculator function from Cramer equation
def cramer(data):
    '''Calculate pitch from CO2_1 concentration'''
    calc_freq = a0 + ((a9*data)/100) + a14*((data)**2) 
    return(calc_freq)

#Run the function for the input column (CO2 values) to get a new column of calculated_frequency
env['calc_freq'] = cramer(env['CO2_1'])

#Import the measured pitch values--the output of pitch_data.py script
pitch = pd.read_table('..data/pitch_data.csv, sep=',')



#Function to make and save a plot


#Close main function
main()
	



