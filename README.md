# Weather Data and SQLite Database

## Project Overview
Analyzing a weather data set for the island of Oahu, Hawaii in order to understand whether a surf and ice cream shop business would be sustainable year-round. Specifically, with the use of SQLAlchemy, the objective is to connect to the SQLite database and query the temperature data for the months of June and December.

## Objectives
- Deliverable 1: Determine the Summary Statistics for June
- Deliverable 2: Determine the Summary Statistics for December

## Softwares
- Python, Pandas in Jupyter Notebook 6.4.12
- SQLAlchemy and SQLite Database

## Analysis
The code to query the SQLite database can be found here: [SurfsUp_Challenge](https://github.com/MSF2141/surfs_up/blob/09bd8e1c0dc15ade67407672353d7e724f4eccb0/SurfsUp_Challenge.ipynb).

Summary statistics for the month of June and December are shown below:

![June%20temps](https://github.com/MSF2141/surfs_up/blob/052482211893bf9297fb72676bf727fce9b49dc6/June%20temps.png) ![December%20temps](https://github.com/MSF2141/surfs_up/blob/3772d6d781630978919ec9c4cd865b377f04c275/December%20temps.png)

## Results
Overall, the analysis of central tendency and spread show similar temperature observations for the month of June and December. For example, results show that average temperature is 75F and 71F for the month of June and December, respectively. The min temperarure observed is 64F and 60F for the month of June and December, respectively. The max temperature observed is 81F and 78F for the month of June and December, respectively. 

## Summary and Future Analysis
Analysis of the weather data set based on the summary statistics indicate that temperature observations for the month of June and December are very similar. Summary statistics, however, depicts the central tendency and spread of a data set. Because the current weather data set is a contineous data set, I would recommend to use a histogram in order to display the frequency distribution of temperature observations. In addition, I would inquire about other weather parameters, such as precipitations and wind speed. It may be possible that temperature does not oscillate much at the island while rain and wind do; consequently affecting the ideal surfing conditions and the ice cream business.

For the sake of an example, I am providing below a histogram of temperature observations for the month of June and December. 
![June%20temps](https://github.com/MSF2141/surfs_up/blob/003b03c034175d6f9ee8fc8107d2e17c96106770/June%20temps_histogram.png) ![December%20temps_histogram](https://github.com/MSF2141/surfs_up/blob/95044b0ba0fc9f1abaeb03d7f422482e1bc539eb/December%20temps_histogram.png)

A histogram of precipitation measurements for the month of June and December shown below:
![June%20prcp_histogram](https://github.com/MSF2141/surfs_up/blob/50162dc2b3f15fedd9c91f511c3c73add02c8d77/June%20prcp_histogram.png) ![December%20prcp_histogram](https://github.com/MSF2141/surfs_up/blob/bb55a39a448c2d193c9e19fd770831bddcde90ae/December%20prcp_histogram.png)

