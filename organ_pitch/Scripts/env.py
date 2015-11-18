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

#I open my main function
def main():

#Upload environmental data file
	env = pd.read_table(input_file, sep=',')

#assign env columns names
	env.columns=[['test', 'date_time','temp C', 'RH %', 'CO2_1', 'CO2_2']]	

#change env data time variable to actual values of time. 
	env['date_time']= pd.to_datetime(env['date_time'])

#Upload measured pitch data
	measured_freq = pd.read_table(pitch_input, sep=',')

#change pitch data time variable to actual values of time.
	measured_freq['time']= pd.to_datetime(measured_freq['time'])

#FUNCTIONS
#test function
	#def test_cramer():
    		#assert a0 + ((a9)*400)/100 + a14*((400/1000000)**2) == 672.339644669, 'Equation failure, math-mess-up'
    		#return()
       
#Cramer equation pitch calculator function 
	def cramer(data):
    		'''Calculate pitch from CO2_1 concentration'''
    		calc_freq = a0 + ((a9*data)/100) + a14*((data)**2) 
    		return(calc_freq)

#Function to make and save a plot
	def make_plot(variable_1, variable_2):
    		'''Make a three variable plot with two axes'''
#plot title
	plt.title('CO2 and Calculated Pitch', fontsize='14')

#twinx layering of curves on single plot
	ax1=plt.subplot()
	ax2=ax1.twinx()
	#ax3=ax1.twinx()

#call data for the plot
	ax1.plot(CO2_1, color='g', linewidth=1)
	ax2.plot(calc_freq, color= 'm', linewidth=1) 
	#ax3.plot(measured_freq)

#axis labeling
	ax1.yaxis.set_tick_params(labelcolor='grey')
	ax1.set_xlabel('Sample Number')
	ax1.set_ylabel('CO2 (ppm)', fontsize=12, color = 'g')
	ax2.set_ylabel('Calculated Pitch (Hz)', fontsize=12, color='m')
	#ax3.set_ylabel('Measured Pitch')

#axis limits
	ax1.set_ylim([400,1300])
	ax2.set_ylim([600, 1500])

#Save the figure as output_plot_name
	plt.savefig(output_plot_name)

#Close function
	return()

#CALL FUNCTIONS
#test function
        #test_cramer()
#Cramer freq function
	cramer(env['CO2_1'])
#Make plot
	make_plot(env, measured_pitch)


#Close main function
main()
	



