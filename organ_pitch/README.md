# CO2 and Pitch Change of a Pipe Organ
### T. Martz-Oberlander, 2011-11-08
### Readme file for my final project root repository

How is the pitch of a pipe organ affected by change in CO2 concentration? This project computes pitch and CO2 data to look at the change in the speed of sound from a pipe organ as CO2 concentration (ppm) changes in a chapel in New Hampshire, USA.

Here I will describe the framework for this repository and provide an outline of the scripts used for my project. This repository was created by running the "Talia Directory Creator" script inside the root repository, "t_final_project".

This root directory holds all scripts of code, raw data files, written analysis documents, figures, and notes on the computational process used for this organ_pitch project. This project looks at CO2 concentration and change in pitch of a pipe organ. 

This computational project is conducted as so:

1) Import data of CO2 concentration and organ pitch; location specific. The data originates in .hobo files which can be converted to .csv files for import to terminal.

2) Compute new columns of data for sound speed from pitch data. Equations for computation come from Cramer (1992) for the mathematical relationship between pitch of a note played on the organ to the frequency of sound waves as they travel through the air in the pipe organ's chapel. Python functions that utilize this math are created to form these new columns.

3) Merge data into dataframes for comparison of sound speed and CO2 concentration levels. Using the new column of sound speed, I can merge and match data columns of CO2 concentration (parts per million) with time-dependant samplings of sound speed. Data points for CO2 and sound speed much be matched based on spacial sampling and time of sample taken.

4) Create plots of these relationships. I can then generate plots to answer meaningful questions about time and space dependancy based on the intricacy of the layout of the chapel and where the samples were collected from.

5) Statistically analyze the CO2/sound relationship. I will look for correlation relationships in a non-normal dataset; as seen in "Analyzing_Data.ipynb" in the "Scripts" directory.

6) Store the different dataframes I created in a "data" directory for later use, and/or to include appendices of raw data in publications.

All needed scripts can be run with the Makefile, located in the main directory "organ_pitch"

 
