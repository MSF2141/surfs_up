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
The code to query the SQLite database can be found here: [SurfsUp_Challenge](https://github.com/MSF2141/surfs_up/blob/57d6433a479e5c4293fef094ede3de805ea0ce68/SurfsUp_Challenge.ipynb).

Summary statistics for the month of June and December are shown below:

![June%20temps](https://github.com/MSF2141/surfs_up/blob/052482211893bf9297fb72676bf727fce9b49dc6/June%20temps.png) ![December%20temps](https://github.com/MSF2141/surfs_up/blob/3772d6d781630978919ec9c4cd865b377f04c275/December%20temps.png)

## Results
Overall, the analysis of central tendency and spread show similar temperature observations for the month of June and December. For example, results show that average temperature is 75F and 71F for the month of June and December, respectively. The min temperarure observed is 64F and 60F for the month of June and December, respectively. The max temperature observed is 81F and 78F for the month of June and December, respectively. 

## Future Analysis
Analysis of the weather data set based on the summary statistics indicate that temperature observations for the month of June and December are very similar. Summary statistics, however, depicts the central tendency and spread of a data set. Because the current weather data set is a contineous data set, I would recommend to use a histogram in order to display the frequency distribution of temperature observations. In addition, I would query other weather parameters, such as precipitations and wind speed. It may be possible that temperature per se will not osculate much, however, rain and wind changes can affect the ideal surfing conditions and the ice cream business.

For the sake of example, 

There needs to be enough rain to keep everything green, but not so much that you lose out on that ideal surfing and ice cream weather.


## Summary
Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.
