# CO2 and Pitch Change of a Pipe Organ
### T. Martz-Oberlander, 2011-11-08
### Readme file for my final project root repository

How is the pitch of a pipe organ affected by change in CO2 concentration? This project computes pitch and CO2 data to look at the change in the speed of sound from a pipe organ as CO2 concentration (ppm) changes in a chapel in New Hampshire, USA.

Here I will describe the framework for this repository and provide an outline of the scripts used for my project. This repository was created by running the "Talia Directory Creator" script inside the root repository, "t_final_project".

This root directory holds all scripts of code, raw data files, written analysis documents, figures, and notes on the computational process used for this organ_pitch project. This project looks at CO2 concentration and change in pitch of a pipe organ. 

This computational project is conducted as to:

1) Import and munge data of measured frequency from the pipe organ;

2) Form data into individual dataframes grouped by the location of sampling (for later comparison to environmental quality data);

3) Visualize the change in measured pitch over time;

This is run using the organ_pitch/driver.sh file for the organ_pitch/Scripts/pitch.py script. Output files (new measured pitch .csv dataframe and plotted pitch) are saved in organ_pitch/Data and organ_pitch/Figures, respectively. 

