#T. Martz-Oberlander, 2015-11-15
#Upload and clean environmental data

#Import useful libraries
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

%matplotlib inline

#I open my main function
def main:

#Define input arguments	
	input_file = sys.argv[1]
	#= sys.argv[2]

#Upload environmental data file
	env = pd.read_table(input_file, sep=',')

#assigning columns names
	env.columns=[['test', 'date_time','temp C', 'RH %', 'CO2_1', 'CO2_2']]	

#change data time variable to actual values of time. 
	env['date_time']= pd.to_datetime(env['date_time'])

#define variables for the pitch calculation
a0 = 331.5024
a14 = 29.179762

#test function
def test_cramer(data):
        
#pitch calculator function
def cramer(data):
    '''Calculate pitch from CO2_1 concentration'''
    #calc_pitch = []
    calc_freq = a0 + a14*((data)**2)
 
    return(calc_freq)

#Run the function for the input column (CO2 values)
env['calc_freq'] = cramer(env['CO2_1'])




#Close main function
main()
	



