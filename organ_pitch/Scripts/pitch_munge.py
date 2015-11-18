#T. Martz-Oberlander, 2015-11-15
#Script for wrangling pitch data into a dataframe with media and standard dev. of sound frequencies
# To call this script: $ python Scripts/pitch_munge.py Data/[input_filename] Data/[output_pitch_dataframe_name] 

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
	pitch=pd.read_table(input_filename, sep=',')

#use date/time timestamp values
	pitch['time']= pd.to_datetime(pitch['time'])

#create new column for median frequency from 9 frequency measurements
	pitch['mean_freq'] = np.mean(pitch[['freq1','freq2','freq3', 'freq4', 'freq5', 'freq6', 'freq7', 'freq8', 'freq9']], axis=1)	

#do the same for standard deviation
	pitch['stdev_freq'] = np.std(pitch['mean_freq'])

#select rows of the pitch dataframe for single div's (sections) of the chapel
	organized_pitch = pitch.groupby(['div']).get_group('choir')

#save this dataframe as a file that can be called in later scripts
	organized_pitch.to_csv(output_pitch_dataframe, sep=',') 	

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

	#Save the figure
	plt.savefig(output_pitch_fig)

        #Close visualization function
	return()

#Call visualization function
	make_plot(organized_pitch)

#Save the figure to the 3rd argument
#plt.savefig(output_pitch_fig)

#close main function
main()




