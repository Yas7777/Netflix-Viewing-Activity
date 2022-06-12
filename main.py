import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
import matplotlib
import pytz
from datetime import datetime, timezone, date
import datetime

# Setting seaborn as default style even if only matplotlib is used
sns.set(style="white")

# Input the netflix file here
netflix = '/Users/yasmeen/Desktop/ViewingActivity.csv'
# read the file
df = pd.read_csv(netflix)

# Pandas dataframe.isna() function is used to detect missing values.
df = df[df['Supplemental Video Type'].isna()]
# Convert default duration HH:MM:SS to number of minutes
df['duration_minutes'] = pd.to_timedelta(df['Duration']).dt.total_seconds()/60
# only include viewings with at least 15 minutes duration
df = df[df['duration_minutes'] >= 15]
# remove columns that will not be used for this project
df.drop("Bookmark", axis=1, inplace=True)
df.drop("Latest Bookmark", axis=1, inplace=True)
df.drop("Attributes", axis=1, inplace=True)

# Graph 1 - How many minutes have the profiles watched?
# Total minutes summed across all years
profile_count = df["Profile Name"]
duration_minutes = df['duration_minutes']
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['Year'] = df['Start Time'].dt.year
df['Month'] = df['Start Time'].dt.month
df = df[df['Year'] != 2015]
df = df[df['Year'] != 2022]
year = df['Year']

# setting the size and style of chart
figure_1 = plt.figure(figsize=(10, 6))
chart = sns.barplot(
    x=year,
    y=duration_minutes,
    hue=profile_count,
    data=df,
    estimator=sum,
    palette="PuRd",
    ci=None
    )
# sum = df['duration_minutes'].sum()
# print(sum)

plt.title("Viewing Frequency", fontsize=14)
plt.xlabel("Years")
plt.ylabel("Number of Minutes")
# Add labels to the bar chart
for container in chart.containers:
    chart.bar_label(container, size=8)
chart.margins(y=0.1)
plt.tight_layout()
plt.show()

show_details = df.Title.str.split(":", expand=True, n=2)
# show_detail split into Show Name, Season, Episode Name
df['show_name'] = show_details[0]
df['Season'] = show_details[1]
df['Episode Name'] = show_details[2]

# If the season column is "None" them it is most likely a movie, lets add another column to our dataframe
# my_history[my_history['season'].isna()]
df['Show Type'] = df.apply(lambda x:'Movie' if pd.isnull(x['Season']) else 'TV Show', axis=1)


# % of movies vs TV shows I have watched - stacked bar
# only use my Profile
df = df[df['Profile Name'] == "Yasmeen"]
for i in df.columns:
    null_rate = df[i].isna().sum()/len(df) * 100
    if null_rate > 0:
        print("{} null rate: {}%".format(i, round(null_rate, 2)))

show_type = df.groupby(['Year', 'Show Type'])['duration_minutes'].sum().unstack()
plt.figure(figsize=(10, 6))
plt.xticks(rotation=0, ha='center')

# First plot the 'Male' bars for every day.
fig, ax = plt.subplots(1)
ax.bar(show_type.index, show_type['TV Show'], label='TV Show', color='pink')
# Then plot the 'Female' bars on top, starting at the top of the 'Male' bars.
ax.bar(show_type.index, show_type['Movie'], bottom=show_type['TV Show'],
       label='Movie', color="red")
ax.legend()
for c in ax.containers:
    # Optional: if the segment is small or 0, customize the labels
    labels = [v.get_height() if v.get_height() > 0 else '' for v in c]
    # remove the labels parameter if it's not needed for customized labels
    ax.bar_label(c, fmt='%0.0f', label_type='center')
ax.set_title('TV Shows vs Movies')
# Remove 'Count' ylabel.
ax.set_ylabel(None)
plt.tight_layout()

# deleting the empty plot for now
plt.close(1)
plt.show()

# Most watched TV Shows

TVshow_groupby = df.groupby('show_name')['duration_minutes'].sum().reset_index().sort_values(by='duration_minutes',
                                                                                             ascending=False)
# TVshow_groupby['duration_hours'] = TVshow_groupby['duration_minutes']/60
# setting the size and style of chart
plt.figure(figsize=(10, 6))
ax = sns.barplot(
    y=TVshow_groupby['show_name'][:10],
    x=TVshow_groupby['duration_minutes'][:10],
    palette="PuRd",
    ci=None)
for c in ax.containers:
    # Optional: if the segment is small or 0, customize the labels
    labels = [v.get_height() if v.get_height() > 0 else '' for v in c]

    # remove the labels parameter if it's not needed for customized labels
    ax.bar_label(c, fmt='%0.0f', label_type='edge')

plt.title("Top 10 TV Shows by Duration")
plt.xlabel("")
plt.ylabel("Frequency of Watching")
plt.show()


# heatmap
# lets work on a new data frame that is copy paste this frame
# we need the years and months

# Convert Start Time to datetime. Currently it is an object
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['Year'] = df['Start Time'].dt.year
df['Month'] = df['Start Time'].dt.month
# df['Day of Week'] = df['Start Time'].dt.dayofweek
# df['Day'] = df['Start Time'].dt.day_name()
df = df[df['show_name'] == 'Friends']
df = df[df['Year'] != 2021]
# create a copy of the dataframe, and add columns for month and year
df_m = df.copy()
# group by month and year, get the sum
df_m = df_m.groupby(['Year', 'Month']).sum()
df_m = df_m.unstack(level=0)

# pd.set_option("display.max_rows", None, "display.max_columns", None)
# fig, ax = plt.subplots(figsize=(11, 9))
# plot heatmap
x_axis_labels = [2016, 2017, 2018, 2019]
sns.heatmap(df_m,
            cmap="PuRd",
            annot=True,
            fmt="0.0f",
            vmin=25,
            vmax=2700,
            linewidth=0.3,
            cbar_kws={"shrink": .8},
            annot_kws={"size": 7},
            xticklabels = x_axis_labels
            )

plt.show()
matplotlib. pyplot. show()