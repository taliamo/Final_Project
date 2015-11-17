#T. Martz-Oberlander, 2015-11-15
#Script for wrangling pitch data into a dataframe with media and standard dev. of sound frequencies
# To call this script: $ python Scripts/pitch_data.py Data/[input_filename] Data/[output_pitch_dataframe_name] 

#Import useful libraries
import pandas as pd
import numpy as np
import sys

# I definte my arguments (input and output)
input_filename = sys.argv[1]
output_pitch_dataframe = sys.argv[2]

#I open my main function
def main():

#import pitch data file
	pitch=pd.read_table(input_filename, sep=',')

#use date/time timestamp values
	pitch['time']= pd.to_datetime(pitch['time'])

#create new column for median frequency from 9 frequency measurements
	pitch['median_freq'] = np.mean(pitch[['freq1','freq2','freq3', 'freq4', 'freq5', 'freq6', 'freq7', 'freq8', 'freq9']], axis=1)	

#do the same for standard deviation
	pitch['stdev_freq'] = np.std(pitch['median_freq'])

#select rows of the pitch dataframe for single div's (sections) of the chapel
	organized_pitch = pitch.groupby(['div']).get_group('choir')

#save this dataframe as a file that can be called in later scripts
	organized_pitch.to_csv(output_pitch_dataframe, sep=',') 	

#close main function
main()




