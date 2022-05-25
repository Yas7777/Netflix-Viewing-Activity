import matplotlib as mlt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
from matplotlib import pyplot
import pytz
from datetime import datetime, timezone
import datetime
sns.set()

# how many minutes of TV I have watched - line chart?
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

# TODO:Supplemental Video Type - only
df = df[df['Supplemental Video Type'].isna()]

# graph of viewing activity
profile_count = df["Profile Name"].value_counts()
plt.figure(figsize=(8,5))
plt.bar(profile_count.index, profile_count.values, color="pink")
plt.ylabel("Freq", fontsize=14)
plt.xlabel("Profile Names", fontsize=14)
plt.xticks(fontsize=11)
plt.title("Viewing Frequency", fontsize=16)





# make a new dataframe'
dfl = df[df['Profile Name'] == 'Yasmeen']

show_details = df.Title.str.split(":", expand=True, n=2)
# show_detail
dfl['Show name'] = show_details[0]
dfl['Season'] = show_details[1]
dfl['Episode Name'] = show_details[2]

# If the season column is "None" them it is most likely a movie, lets add another column to our dataframe
# my_history[my_history['season'].isna()]
dfl['Show Type'] = dfl.apply(lambda x:'Movie' if pd.isnull(x['Season']) else 'TV Show', axis=1)


x = dfl.groupby(['Show Type'])['Show Type'].count()
y = len(dfl)
r = ((x/y)).round(2)
mf_ratio = pd.DataFrame(r).T
