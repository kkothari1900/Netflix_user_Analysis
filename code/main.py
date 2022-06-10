#Packages:
import os
import pandas as pd
import numpy as np
import matplotlib
import csv
from tabulate import tabulate
import matplotlib.pyplot as plt


# Certain working directory
cwd = os.getcwd()

print("Current working directory: {0}".format(cwd))
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))

# Importing data
view_activ = pd.read_csv(r'ViewingActivity.csv')
view_activ = pd.DataFrame(view_activ)
#print(view_activ)


# Only looking at viewing data from Kareena's profile:
user_titles = view_activ[['Profile Name','Title','Start Time','Duration']]
user_titles = pd.DataFrame(user_titles)

#print(user_titles)

# Renaming the profile name variable:

user_titles.rename(columns = {'Profile Name':'Profile_Name'},inplace = True)
user_titles.rename(columns = {'Start Time':'Start_Time'},inplace = True)
#print(user_titles)

Kareenas_titles = user_titles[user_titles.Profile_Name == 'Kareena']
print(Kareenas_titles.head())
#Kareenas_titles.to_csv('KareenasData2.csv')




print(Kareenas_titles)
#print(Kareenas_titles.dtypes)

# Start time converting to time zone attached utc = True
Kareenas_titles['Start_Time'] = pd.to_datetime(Kareenas_titles['Start_Time'], utc=True)
#print(Kareenas_titles.dtypes)


# Start time column into the data frame index
Kareenas_titles = Kareenas_titles.set_index('Start_Time')
Kareenas_titles.index = Kareenas_titles.index.tz_convert('US/Pacific')
Kareenas_titles = Kareenas_titles.reset_index()
print(Kareenas_titles.head(1))
print(Kareenas_titles.head())
#Kareenas_titles.to_csv('KareenasData2.csv')


# Duration Conversion
Kareenas_titles['Duration'] = pd.to_timedelta(Kareenas_titles['Duration'])
# Checking the data types
print(Kareenas_titles.dtypes)


# Watch List frequency Table:
#Kareenas_titles_freq = pd.crosstab(Kareenas_titles['Title'],'no_of_times_watched')
#print(tabulate(Kareenas_titles_freq))

# Splitting/ new data frame of start time seperated from date

#Kareena_tit_2 = Kareenas_titles["Start_Time"].str.split("", n=1, expand=True)
#Kareenas_titles["Date"] = Kareena_tit_2[1]
#Kareenas_titles["Time"] = Kareena_tit_2[2]
#Kareenas_titles.drop(columns = ["Start_Time"],inplace = True)
#print(Kareena_tit_2.head())
#Kareena_tit_2.to_csv('KareenasData3.csv')


Kareenas_titles['Start_Time'] = Kareenas_titles["Date"].astype(str)
Kareenas_titles['Start_Time'] = Kareenas_titles["Time"].astype(str)
Kareenas_titles["Date"] = Kareenas_titles['Start_Time'].str[0:2]
Kareenas_titles["Time"] = Kareenas_titles['Start_Time'].str[2:4]

Kareenas_titles.drop('Start_Time',axis=1,inplace=True)

print(Kareenas_titles.head(1))


# Checking for Gilmore Girls
Gilmore_Girls = Kareenas_titles[Kareenas_titles['Title'].str.contains('Gilmore Girls:', regex=False)]
print(Gilmore_Girls.shape)


# Checking For New Girl
New_Girl = Kareenas_titles[Kareenas_titles['Title'].str.contains('New Girl:', regex=False)]
print(New_Girl.shape)


# Checking for Jane the Virgin
Jane_The_Virgin = Kareenas_titles[Kareenas_titles['Title'].str.contains('Jane The Virgin:', regex=False)]
print(Jane_The_Virgin.shape)

# Checking for Greys Anatomy
Greys_Anatomy = Kareenas_titles[Kareenas_titles['Title'].str.contains("Grey's Anatomy:", regex=False)]
print(Greys_Anatomy.shape)



# How much time have I spent watching Gilmore Girls, New Girl, and Jane The Virgin?

#print(Gilmore_Girls['Duration'].sum()) # Output 17 days: 15 hours, 54 minutes, 14 seconds
#print(New_Girl['Duration'].sum()) # Output 13 Days: 7 hours, 9 minutes, 12 seconds
#print(Jane_The_Virgin['Duration'].sum()) # Ouput 11 days: 6 hours, 6 minutes, 12 seconds
#print(Greys_Anatomy['Duration'].sum()) #Output 23 Days: 5 Hours, 22 minutes, 40 seconds

# When do I watch Gilmore Girls?
Gilmore_Girls['weekday'] = Gilmore_Girls['Start_Time'].dt.weekday
Gilmore_Girls['hour'] = Gilmore_Girls['Start_Time'].dt.hour

# When do I watch New Girl?
New_Girl['weekday'] = New_Girl['Start_Time'].dt.weekday
New_Girl['hour'] = New_Girl['Start_Time'].dt.hour
print(New_Girl.head(1))

# When do I watch Jane The Virgin?
Jane_The_Virgin['weekday'] = Jane_The_Virgin['Start_Time'].dt.weekday
Jane_The_Virgin['hour'] = Jane_The_Virgin['Start_Time'].dt.hour
print(Jane_The_Virgin.head(1))


# When do I watch Greys Anatomy?
Greys_Anatomy['weekday'] = Greys_Anatomy['Start_Time'].dt.weekday
Greys_Anatomy['hour'] = Greys_Anatomy['Start_Time'].dt.hour
print(Greys_Anatomy.head(1))









# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
