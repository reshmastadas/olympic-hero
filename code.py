# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here

# Loding data 
data = pd.read_csv(path)

# Renaming column Total to Total_Medals
data.rename(columns={"Total":"Total_Medals"},inplace=True)

# displaying first 10 records
print(data.head(10))


# --------------
#Code starts here

# creating column Better_Event which stores 'summer', 'winter' or 'both'
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer',np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both'))

# Finding better event wrt all performing countries 
max_value = ((data.Better_Event.value_counts()).max())
better_event = data.Better_Event.value_counts()[data.Better_Event.value_counts()==max_value].index[0]
print(better_event)


# --------------
#Code starts here

# Creating dataframe top_countries with columns 'Country_Name','Total_Summer', 'Total_Winter','Total_Medals'
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

# dropping last row from top_countries
top_countries.drop(index = top_countries.tail(1).index, inplace = True)

# definition of function that return list of top 10 countries
def top_ten(top_countries, col_name):
    """-------Function top ten--------
    input: dataframe, column name
    returns: Returns list of top 10 rows of dataframe based on the input column"""
    
    country_list = list((top_countries.nlargest(10, col_name))['Country_Name'])
    return country_list

# calculating top_10_summer, top_10_winter, top_10
top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

# finding common contries in all the three lists
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)


# --------------
#Code starts here
# Subsetting dataframe wrt top_10_summer, top_10_winter, top_10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

# Plotting bar graphs
fig, ax = plt.subplots(3, sharex=True)
ax[0].bar(summer_df['Country_Name'],summer_df['Total_Summer'])
ax[0].set_title('top 10 country vs summer medals')
ax[1].bar(winter_df['Country_Name'],winter_df['Total_Winter'])
ax[1].set_title('top 10 country vs winter medals')
ax[2].bar(top_df['Country_Name'],top_df['Total_Medals'])
ax[2].set_title('top 10 country vs total medals')



# --------------
#Code starts here

# creating column Golden_Ratio in summerdf
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']

# finding country with maximum golden ratio in summer dtaframe
summer_max_ratio = np.max(summer_df['Golden_Ratio'])
summer_country_gold = str((summer_df[summer_df['Golden_Ratio']==summer_max_ratio].Country_Name).iloc[0])

# creating column Golden_Ratio in winterdf
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']

# finding country with maximum golden ratio in winter dtaframe
winter_max_ratio = np.max(winter_df['Golden_Ratio'])
winter_country_gold = str((winter_df[winter_df['Golden_Ratio']==winter_max_ratio].Country_Name).iloc[0])

# creating column Golden_Ratio in top_df
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']

# finding country with maximum golden ratio in top dtaframe
top_max_ratio = np.max(top_df['Golden_Ratio'])
top_country_gold = str((top_df[top_df['Golden_Ratio']==top_max_ratio].Country_Name).iloc[0])


# --------------
#Code starts here

# dropping last row from data and asigning it to data_1
data_1 = data[:-1]

# finding weighted sum of gold, silver and bronze medals
data_1['Total_Points'] = (3*(data_1['Gold_Total']))+(2*(data_1['Silver_Total']))+data_1['Bronze_Total']

# finding best country and its total points
most_points = data_1['Total_Points'].max()
best_country = str((data_1[data_1['Total_Points']==most_points].Country_Name).iloc[0])


# --------------
#Code starts here

# Creating best dataframe
best = data[data['Country_Name']==best_country]

# selecting only necessary columns
best = best[['Gold_Total','Silver_Total','Bronze_Total']]

# Creating a bar graph
best.plot.bar(stacked = True)

# adding labels
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)


