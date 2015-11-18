#T. Martz-Oberlander, 2015-11-15
#Script for wrangling pitch data into a dataframe with media and standard dev. of sound frequencies
# To call this script: $ python Scripts/pitch_munge.py Data/[input_filename] Data/[output_pitch_dataframe_name] Figures/[output_pitch_fig_name]

#Import useful libraries
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt

# I definte my arguments (input and output)
input_filename = sys.argv[1]
output_pitch_dataframe = sys.argv[2]
output_pitch_fig = sys.argv[3]

#I open my main function
def main():

#import pitch data file
	pitch = pd.read_table(input_filename, sep=',')

#use date/time timestamp values
	pitch['time'] = pd.to_datetime(pitch['time'])

#create new column for mean frequency from 9 frequency measurements
	pitch['mean_freq'] = np.mean(pitch[['freq1','freq2','freq3', 'freq4', 'freq5', 'freq6', 'freq7', 'freq8', 'freq9']], axis=1)

#Test to see if data is a float, and useable in a plot

def test_data_type(data):
    '''Check to see if a column contains only floats'''
    obs = pitch['freq7'].dtype #I pass the dtype checking function through my test function
    #print(obs)
    exp = 'float64'
    assert obs == 'float64', 'Data is not a float'
    return

#Call the test function on the 'freq5' column in the 'pitch' dataframe
test_data_type(pitch['freq5'])

#do the same for standard deviation
pitch['stdev_freq'] = np.std(pitch['median_freq'])

#select rows of the pitch dataframe for single div's (sections) of the chapel
organized_pitch = pitch.groupby(['div']).get_group('choir')

#save this dataframe as a file that can be called in later scripts
organized_pitch.to_csv(output_pitch_dataframe, sep=',')
	
#Function to plot the new dataframe for one chapel section 
def make_plot(data):
	'''Make line plot for measured pitch'''
#Plot figure of change in pitch over time 
	plt.figure(figsize=(8,5))

	#Select data
	fig = plt.plot(organized_pitch['time'], organized_pitch['mean_freq'], color = 'navy')

	#Make title and labels for plot
	plt.title('Pitch of C5 Pipe Organ Note')
	plt.ylabel('Sound Frequency (Hz)')
	plt.xlabel('Time of Sample Taken (Apr. 13, 16, and 17, 2010)')

	#Save figure in Figures	
	plt.savefig(output_pitch_fig)
	
	#Close visualization function
	return()

#Call visualization function 
	make_plot(organized_pitch) 

#close main function
main()


