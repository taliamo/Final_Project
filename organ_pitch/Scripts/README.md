# T. Martz-Oberlander, 2015-11-08
# Scripts information
# All script files for the organ pitch project are stored 
#in this "Scripts" repository.

Scripts contain code for:
Uploading data;

Sorting and rearranging data ("pitch_munge.py" and "env_data.py");

Finding mean values and standard deviation for musical note frequency (same as above);

Visualizing data ( "env_data.py");

Running statistical tests on data ("stats_compare.py");

There is a Makefile while acts as a driver script to run the other scripts. It includes a "make clean" command, which can reset the directories for the scripts to be re-run. 

The commands for the first script, "pitch_munge.py" are: $ python Scripts/pitch_data.py Data/[input_filename] Data/[output_pitch_dataframe_name]

The commands for the second script, "env_data.py" are: $ python Scripts/env_data.py Data/[input filename] Figures/[output plot name] 

To run through the entire project, use the Makefile.


