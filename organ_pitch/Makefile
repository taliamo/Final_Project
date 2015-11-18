#T. Martz-Oberlander, 2015-11-13
##Makefile for organ pitch project
##Runs pitch munger, environmental munger, and plot maker scripts; cleans directory

# all : Scripts/pitch_munge2.py  Data/pitches.csv

#Pitch munging
Data/munged_pitch2.csv : Data/pitches.csv
        python Data/pitches.csv Data/munged_pitch.csv

#clean (Delete .pdf figures, and numbered munged_pitch.csv files made previously)
.PHONY : clean
clean :
        rm -f organ_pitch/Figures/*.pdf
        rm -f organ_pitch/Data/*munged_pitch.csv




