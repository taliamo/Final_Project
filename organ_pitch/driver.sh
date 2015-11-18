#!/bin/bash 

#Cleanr directories
#rm ./Figures/*.pdf
#rm ./Data/munged_pitch.csv

#Generalized arguments for input datafile, output .csv dataframe, and output figure name
python ./Scripts/pitch_munge.py $1 $2 $3



 
