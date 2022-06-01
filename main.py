import matplotlib as mlt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
from matplotlib import pyplot
import pytz
from datetime import datetime, timezone
from datetime import date
import datetime
sns.set(style="white")
from datetime import datetime, timezone
import pytz
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt
import seaborn as sb



from datetime import date
from datetime import datetime

import requests
from bs4 import BeautifulSoup
import re

# how many minutes of have the profiles watched - ?
# % of movies vs TV shows I have watched - stacked bar
# Top 10 Binge-Watching TV Series - bar graph
# HeatMap of my Viewing Activity of one show - Friends


# Input the netflix file here
netflix = '/Users/yasmeen/Desktop/ViewingActivity.csv'
# read the file
df = pd.read_csv(netflix)

# Convert duration HH:MM:SS to number of minutes
df['duration_minutes'] = pd.to_timedelta(df['Duration']).dt.total_seconds()/60

# only include viewings with at least 15 minutes duration
df = df[df['duration_minutes'] >= 15]

# remove columns that mean nothing
df.drop("Bookmark", axis=1, inplace=True)
df.drop("Latest Bookmark", axis=1, inplace=True)
df.drop("Attributes", axis=1, inplace=True)
#print(df)
# how many minutes of have the profiles watched - ?
profile_count = df["Profile Name"].value_counts()
# setting the size of figure
plt.figure(figsize=(10, 6))
sns.barplot(
    x=profile_count.index,
    y=profile_count.values,
    data=df,
    estimator=sum)
plt.title("Viewing Frequency", fontsize=16)
plt.xlabel("Profile Names")
plt.ylabel("Number of minutes")
sns.despine()
#plt.show()

# % of movies vs TV shows I have watched - stacked bar
# TODO:Supplemental Video Type - only
# Pandas dataframe.isna() function is used to detect missing values.
df = df[df['Supplemental Video Type'].isna()]
#print(df)
show_details = df.Title.str.split(":", expand=True, n=2)
# show_detail
df['Show name'] = show_details[0]
df['Season'] = show_details[1]
df['Episode Name'] = show_details[2]

# If the season column is "None" them it is most likely a movie, lets add another column to our dataframe
# my_history[my_history['season'].isna()]
df['Show Type'] = df.apply(lambda x:'Movie' if pd.isnull(x['Season']) else 'TV Show', axis=1)

# Take only
df = df[df['Profile Name'] == 'Yasmeen']


x = df.groupby(['Show Type'])['Show Type'].count()
print(x)
y = len(df)
ratio = ((x/y)).round(2)
# todo:what do this do?
mf_ratio = pd.DataFrame(ratio).T
for i in df.columns:
    null_rate = df[i].isna().sum()/len(df) * 100
    if null_rate > 0 :
        print("{} null rate: {}%".format(i,round(null_rate,2)))

#todo: how to do a stacked graph of % seaborn
# % of movies vs TV shows I have watched - stacked bar
#plt.figure(figsize=(10, 6))
#ax = plt.subplots(1,1)
fig, ax = plt.subplots(1,1,figsize=(6.5,2.5))
ax.barh(mf_ratio.index, mf_ratio['Movie'],
        color='#b20710', alpha=0.9, label='Male')
ax.barh(mf_ratio.index, mf_ratio['TV Show'], left=mf_ratio['Movie'],
        color='#221f1f', alpha=0.9, label='Female')
ax.set_xlim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
#plt.show()

# Most number of- NUMBER OF SEASONS
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
ax = sns.barplot(x=df['Show name'].sort_values(ascending=True).value_counts().index[:10],
                 y=df["Show name"].sort_values(ascending=True).value_counts()[:10])
plt.title("Shows with most time spent")
plt.xlabel("Name of Show")
plt.ylabel("Frequency of Watching")
loc, labels = plt.xticks()
ax.set_xticklabels(labels, rotation=45)
#plt.show()



TVshow_groupby = df.groupby(by='Show name').sum()
print(TVshow_groupby)

TVshow_groupby = TVshow_groupby.sort_values('duration_minutes', ascending=False)
print(TVshow_groupby)
TVshow_groupby['duration_hours'] = TVshow_groupby['duration_minutes']/60
print(TVshow_groupby)

plt.figure(figsize=(10,5))
most_watched = TVshow_groupby.head(5)
plt.barh(most_watched.index, most_watched['duration_hours'])
plt.xlabel('Watched hours')
plt.show()
#heatmap

#lets work on a new data frame that is copy paste this frame
#we need the years and months

#Convert Start Time to datetime. Currently it is object
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['Year'] = df['Start Time'].dt.year
df['Month'] = df['Start Time'].dt.month
#df['Day of Week'] = df['Start Time'].dt.dayofweek
#df['Day'] = df['Start Time'].dt.day_name()
df = df[df['Show name'] == 'Friends']
df = df[df['Year']!= 2021]
print(df)
#create a copy of the dataframe, and add columns for month and year
df_m = df.copy()
# group by month and year, get the average
df_m = df_m.groupby(['Month', 'Year']).sum()
print(df_m)
df_m = df_m.unstack(level=0)

print(df_m)
#pd.set_option("display.max_rows", None, "display.max_columns", None)
fig, ax = plt.subplots(figsize=(11, 9))

# plot heatmap
sb.heatmap(df_m, cmap="Blues", vmin= 100, vmax=500,linewidth=0.3, cbar_kws={"shrink": .8})
plt.show()


