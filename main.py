import matplotlib as mlt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# netflix file
netflix = '/Users/yasmeen/Desktop/ViewingActivity.csv'
# read the file
df = pd.read_csv(netflix)
# remove Supplemental Video Type coloumn
del df['Supplemental Video Type']
columns_to_drop = ["Country", "Bookmark", "Latest Bookmark", "index", "Attributes", "Supplemental Video Type"]
my_data = df.drop(columns = columns_to_drop)

show_details = df.Title.str.split(":",expand=True,n=2)
# show_detail
df['show_name'] = show_details[0]
df['season'] = show_details[1]
df['episode_name'] = show_details[2]

# If the season column is "None" them it is most likely a movie, lets add another column to our dataframe
# my_history[my_history['season'].isna()]
df['show_type'] = df.apply(lambda x:'Movie' if pd.isnull(x['season']) else 'TV Show', axis=1)

# 0:01:05 -> 65
def durationTimeToSeconds(duration):
    try:
        [hour, minutes, seconds] = duration.split(':')
        return int(hour)*3600 + int(minutes)*60 + int(seconds)
    except:
        return 0

# 65 -> 00:01::05
def secondsToDurantion(seconds):
    hours = math.floor(seconds/3600)
    remainingSeconds = seconds - (hours*3600)
    minutes = math.floor(remainingSeconds/60)
    remainingSeconds = remainingSeconds - (minutes*60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, remainingSeconds)
'''
# duration = "00:21:12"
# Convert to minutes = first split the duration into a list by removing ":"
df['duration_minutes'] = df['Duration'].str.split(':')
# Convert to minutes = second i[0]*60 + i[1]
df['duration_minutes'] = df['duration_minutes'].apply(lambda x: int(x[0]) * 60 + int(x[1]))
# filter duration time to only more than 10
df = df[df['duration_minutes'] >= 10]'''

# make a new dataframe'
dfl = df[df['Profile Name'] == 'Yasmeen']

x = dfl.groupby(['Type'])['Type'].count()
y = len(dfl)
r = ((x/y)).round(2)
mf_ratio = pd.DataFrame(r).T