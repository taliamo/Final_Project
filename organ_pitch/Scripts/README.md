# T. Martz-Oberlander, 2015-11-08
## Scripts information
All script files for the organ pitch project are stored 
in this "Scripts" repository.

Scripts contain code for:
uploading data, creating new dataframes, testing data type, plotting and saving figures of measured pitch. 

env.py
env_data.py
pitch_munge.py
pitch_munge2.py 

are all iterations of this project's script which are non functional.

pitch.py is the working script. It can be run by entering " $ bash driver.sh $1 $2 $3" in the command line, where the arguments are: input pitch data file, output pitch dataframe (grouped by location with mean and standard deviation of frequency), and output figure name. Provide directory locations to save the .csv and .pdf files in their appropriate locations (Data and Figures, respectively). Also invlude .csv and .pdf file types at the end of the name for ease of documentation later.


