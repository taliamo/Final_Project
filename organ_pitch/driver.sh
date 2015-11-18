#!/bin/bash 

#Clean directories of new dataframes and figures
#rm ./Figures/*.pdf
#rm ./Data/munged_pitch.csv

#Generalized arguments for input datafile, output .csv dataframe, and output figure name
python ./Scripts/pitch.py $1 $2 $3



 
