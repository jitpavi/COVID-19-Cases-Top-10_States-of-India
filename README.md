# Project Name -  Tracking live Covid-19 cases in all States of India 
#### -- Project Status: [Completed]

## Project Intro/Objective:
The purpose of this project is to produce a combined bar chart for the top 10 states of India currently with the most affected cases of Covid-19 where each bar is displaying Total no of covid cases, Total no. of cured cases and Total no. of Deaths respectively for each states.

### Methods Used:
* Explorative Data Analysis
* Data Wrangling
* Data Visualization

### Technologies:
* Python
* Pandas
* Pycharm
* Matplotlib
* Numpy

## Project Description

### Prerequisites: 
  ### -> Dataset:
  API for accessing data from Government website(https://api.data.gov.in/resource/cd08e47b-bd70-4efb-8ebc-589344934531?    format=viz&limit=all&api-key=579b464db66ec23bdd000001cdc3b564546246a772a26393094f5645&_=1587843731797)
  
  ### -> Python Libraries:
  * Pandas
  * Matplotlib
  * Numpy

### Workflow:
1. Using request module download the data from the govt. website.
2. Convert the response data into JSON obejct.
3. Create a Dataframe using Pandas from the JSON object with columns Death,Total Confirmed cases and Cured/Discharged/Migrated.
4. Sort the dataframe by the column name Total Confirmed cases in descending order.
5. Create a fig subplot and create 3 ax objects where each representing a bar chart for the columns  Total no of covid cases, Total no. of cured cases and Total no. of Deaths respectively
6. Enable annotation on each bar denoting the number of cases.
7. Display the combine bar charts for the top 10 states with the most affected cases.

## Expected Output:

* [Covid-19 Statistics.jpg](https://github.com/jitpavi/Covid-19-Cases-in-States-of-India/blob/master/Covid-19%20Statistics.jpg)

## Featured Notebooks/Analysis/Deliverables:

* [COVID-19 Cases Indian States v1.0.py](https://github.com/jitpavi/Covid-19-Cases-in-States-of-India/blob/master/COVID-19%20Cases%20Indian%20States%20v1.0.py)

## Versioning:

Code version - v1.0

## Authors:

* **Jitin Pavithran** - [jitpavi](https://github.com/jitpavi)

## Acknowledgments:

* https://data.gov.in/major-indicator/covid-19-india-data-source-mohfw
