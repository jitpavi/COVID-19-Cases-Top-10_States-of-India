# Project Name
## Tracking live Covid-19 cases in all States of India 

#### -- Project Status: [Completed]

## Project Intro/Objective
The purpose of this project is to produce a bar chart for the top 10 states of India currently with the most affected cases of Covid-19.

### Methods Used
* Explorative Data Analysis
* Data Wrangling
* Data Visualization

### Technologies
* Python
* Pandas
* Pycharm
* Matplotlib
* Numpy

## Project Description

### Prerequisites 
  ### Dataset - 
  API for accessing data from Government website(https://api.data.gov.in/resource/cd08e47b-bd70-4efb-8ebc-589344934531?    format=viz&limit=all&api-key=579b464db66ec23bdd000001cdc3b564546246a772a26393094f5645&_=1587843731797)
  
  ### Python Libraries 
  * Pandas
  * Matplotlib
  * Numpy

### Workflow
1. Using request module download the data for the city Mumbai.
2. Convert the response data into JSON obejct.
3. Create a Dataframe using Pandas from the JSON object.
4. Derive a resultant column using other columns including Traffic index Live, JamsDelay,Jamscount and JamsLength.
5. Create a Pandas grouby object using Weekday and Hour colum and perform unstack to give a look of pivot table.
6. Using Seaborn create a HeatMap object and import the grouby data as the input

## Expected Output
* [Covid-19 Statistics.jpg](https://github.com/jitpavi/Mumbai_Traffic_Analysis/blob/master/Traffic_HeatMap.jpg)

## Featured Notebooks/Analysis/Deliverables
* [COVID-19 Cases Indian States v1.0.py](https://github.com/jitpavi/Mumbai_Traffic_Analysis/blob/master/Mum-Traffic_Analysisv1.0.py)

## Versioning
Code version - v1.0

## Authors

* **Jitin Pavithran** - [jitpavi](https://github.com/jitpavi)

## Acknowledgments and References

* https://www.tomtom.com/
* https://towardsdatascience.com/scraping-live-traffic-data-in-3-lines-of-code-step-by-step-9b2cc7ddf31f
