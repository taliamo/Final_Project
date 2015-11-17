#T. Martz-Oberlander, 2015-11-15
#Script for wrangling pitch data into a dataframe with media and standard dev. of sound frequencies


#Import useful libraries
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

%matplotlib inline

# I definte my arguments (input and output)
input_file = sys.argv[1]
output_pitch_dataframe = sys.argv[2]

#I open my main function
def main:
#import pitch data file
	pitch=pd.read_table(input_file, sep=',')

#use date/time timestamp values
	pitch['date_time']= pd.to_datetime(pitch['date_time'])

#create new column for median frequency from 9 frequency measurements
	pitch['median_freq'] = np.mean(pitch[['freq1','freq2','freq3', 'freq4', 'freq5', 'freq6', 'freq7', 'freq8', 'freq9']], axis=1)	

#do the same for standard deviation
	pitch['stdev_freq'] = np.std(pitch['median_freq'])

#select rows of the pitch dataframe for single div's (sections) of the chapel
	organized_pitch = pitch.groupby(['div']).get_group('choir')

#save this dataframe as a file that can be called in later scripts
	

#close main function
main()




