"""
Code Name: Detailed Barchart of Covid Cases for Top 10 state of India
Code Author: Jitin Pavithran
Code Version: 1.0
Code Description: This code will generate a combined bar charts displaying the total number of Cases,Cured and Deaths for the Top 10 States of India.
"""

# Import all the relevant important libraries to get the output
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
import time

# Compute the starttime to evaluate the total code execution time
st=time.time()

# Import the data from using the api key provided the government website and create a JSON object out of this.
url2 = r"https://api.data.gov.in/resource/cd08e47b-bd70-4efb-8ebc-589344934531?format=viz&limit=all&api-key=579b464db66ec23bdd000001cdc3b564546246a772a26393094f5645&_=1587843731797"

cov_resp = requests.request("GET",url2)
cov_json = cov_resp.json()

field_items = cov_json['field']
d_cols = []

for fi in field_items:
    d_cols.append(fi['name'])

d_list = cov_json['data']

# Create a dictionary object and import the data in it
dict = {}
for i in range(len(d_cols)):
     dict[d_cols[i]] = [j[i]  for j in d_list]

# Create a dataframe object with the dictionary object imported in it
cov_df = pd.DataFrame(dict)
print(type(cov_df))

# Drop the columns which are not required
cov_df.drop(columns=['Date','DateTime','S. No.'],axis=1,inplace=True)
cov_df.rename(columns=lambda x:x.strip(),inplace=True)

# Convert the object type of column Death,Confirmed cases and Cured Cases in integer datatype
cov_df = cov_df.astype({'Death':'int64','Total Confirmed cases':'int64','Cured/Discharged/Migrated':'int64'})

# Sorted the dataframe according to the values of the column Total Confirmed cases in descending order
cov_df = cov_df.sort_values(by='Total Confirmed cases',ascending=False)

# Create and Figure and ax objects for subplotting
fig,ax = plt.subplots(figsize=(14,7))

# Create width object for the width of each BAR
width = 0.2

# Create a range from 0-9 based corresponding to TOP 10 states
x=np.arange(len((cov_df['Name of State / UT'][:10])))
print(x)

# Create BAR chart object corresponding to each columns Confirmed cases, cure patients and Deaths respectively
r1 = ax.bar(x,cov_df['Total Confirmed cases'][:10],width=width,color='b',label = 'Total No. of Confirmed Cases')
r2 = ax.bar(x+width,cov_df['Cured/Discharged/Migrated'][:10],width=width,color='g',label = 'Total No. of Cured Patients')
r3 = ax.bar(x+(width*2),cov_df['Death'][:10],width=width,color='r',label = 'Total No. of Deaths')
ax.set_xticks(x+width+width/2)

# Replace the values of x with the names of the States/UT
ax.set_xticklabels(cov_df['Name of State / UT'][:10])
ax.set_title('COVID-19 INDIA Data (Top 10 States)')
ax.legend()

# Create function of autolabele for annotation of Figures on each of the BAR going to be displayed in the chart
def autolabels(rects):
    for r in rects:
        h = r.get_height()
        ax.annotate(f'{h}',xy=(r.get_x()+r.get_width()/2,h),ha='left', va='bottom',rotation=60)

# Call the functions for each the BAR
autolabels(r1)
autolabels(r2)
autolabels(r3)

# Compute the total execution time and print on the screen
et = time.time()
print(et-st)

# Save the Bar chart in jpg format in the local drive
plt.savefig(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Covid-19\Stats.jpg")

# Save the Dataframe into CSV file
cov_df.to_csv(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Covid-19\COVID-19.csv",index=False)

# Display the Bar chart
fig.tight_layout()
plt.show()