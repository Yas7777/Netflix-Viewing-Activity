import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Setting seaborn as default style even if only matplotlib is used
sns.set(style="white")

# Input the Netflix file here
netflix_filepath = input("Enter filepath as described in the ReadMe: ")
df = pd.read_csv(netflix_filepath)
# check to see if it prints
print(df)

# Data Clean - Up

# Supplemental Video Type consists of values such as "hook", "trailer" etc which we do not want to include in the data
# analysis. We only want feature length TV Shows/Movies in our DF which has no value. Pandas dataframe.isna() function
# is used to detect missing values. The code below ensure that the DF only consists of data with the missing values i.e.
# only consists of movies and tv shows.

df = df[df['Supplemental Video Type'].isna()]
# Convert default duration HH:MM:SS to number of minutes
df['Duration'] = pd.to_timedelta(df['Duration']).dt.total_seconds()/60
# Only include viewings with at least 15 minutes duration
df = df[df['Duration'] >= 15]
# Converts Duration from Minutes into Hours
df['Duration'] = df['Duration'] / 60
# Remove columns that will not be used for this data analysis.
df.drop("Bookmark", axis=1, inplace=True)
df.drop("Latest Bookmark", axis=1, inplace=True)
df.drop("Attributes", axis=1, inplace=True)

# Show Details needs to be split up into Show name, Season and Episode Name. Currently, in one string. This code below
# splits it into 3 columns
show_details = df.Title.str.split(":", expand=True, n=2)
# show_detail split into Show Name, Season, Episode Name (Column 0, 1, and 2)
df['Show Name'] = show_details[0]
df['Season'] = show_details[1]
df['Episode Name'] = show_details[2]


# If the season column is "None" -> it is a movie, lets add another column to the DF
df['Show Type'] = df.apply(lambda x: 'Movie' if pd.isnull(x['Season']) else 'TV Show', axis=1)
# Convert Start Time to datetime. Currently, it is an object.

df['Start Time'] = pd.to_datetime(df['Start Time'])
# We need the years and months
df['Year'] = df['Start Time'].dt.year
df['Month'] = df['Start Time'].dt.month
# Can include the below to screen for certain years for example:
# if the user only wants to use years that are not = 2015 and 2022
# df = df[df['Year'] != 2015]
# df = df[df['Year'] != 2022]

# ---------------Graph 1 - How many minutes have the profiles watched?-----------------------

# Total duration minutes summed across all years
profile_count = df["Profile Name"]
Duration = df['Duration']

# Count the Years
year = df['Year']

# Sets the SNS bar plot
figure_1 = plt.figure(figsize=(10, 6))
chart = sns.barplot(
    x=year,
    y=Duration,
    hue=profile_count,
    data=df,
    estimator=sum,
    palette="PuRd",
    ci=None
    )

# Sets the format of Graph 1
plt.title("Viewing Frequency", fontsize=14)
plt.xlabel("")
plt.ylabel("Duration (in Hours)")
# Add labels to the bar chart
for container in chart.containers:
    chart.bar_label(container, size=10, fmt='%0.0f')
chart.margins(y=0.1)
plt.tight_layout()
plt.show()

# --------------Graph 2 - Movies vs TV shows------------------------

# only use one Profile
user_profile_name = input("Enter Profile Name: ")
df = df[df['Profile Name'] == user_profile_name]
# Sanity - Check
for i in df.columns:
     null_rate = df[i].isna().sum()/len(df) * 100
     if null_rate > 0:
         print("{} null rate: {}%".format(i, round(null_rate, 2)))

show_type = df.groupby(['Year', 'Show Type'])['Duration'].sum().unstack()

plt.figure(figsize=(10, 6))
plt.xticks(rotation=0, ha='center')

# Plot graph
# First plot the 'TV Show' bars
fig, ax = plt.subplots(1)
ax.bar(show_type.index, show_type['TV Show'], label='TV Show', color='#d4b9da')
# Plot the 'Movie' bars on top, starting at the top of the 'TV Show' bars.
ax.bar(show_type.index, show_type['Movie'], bottom=show_type['TV Show'],
       label='Movie', color='#df65b0')
ax.legend()

for c in ax.containers:
    # Adding labels to the graph
    ax.bar_label(c, size=10, fmt='%0.0f', label_type='center')

plt.title(str(user_profile_name) + " Viewing Frequency - TV Shows vs Movies")
ax.set_ylabel("Duration (in Hours)")
plt.tight_layout()

# deleting the empty plot for now
plt.close(1)
plt.show()

# ---------------Graph 3- Vertical Stacked Graph -  Most watched TV Shows------------------
df_copy = df.copy()
tv_show_groupby = df_copy.groupby('Show Name')['Duration'].sum().reset_index().sort_values(by='Duration',
                                                                                              ascending=False)
print(df)
# setting the size and style of chart
plt.figure(figsize=(10, 6))

# plot graph
ax = sns.barplot(
    x=tv_show_groupby['Duration'][:10],
    y=tv_show_groupby['Show Name'][:10],
    palette="PuRd",
    ci=None)

# Adding labels to the vertical stacked graph
for c in ax.containers:
    ax.bar_label(c, fmt='%0.0f', label_type='edge')

plt.title("Top 10 TV Shows (by duration)")
plt.xlabel("Duration (in Hours)")
plt.ylabel("")
plt.tight_layout()
plt.show()

# ------------Graph 4 - Heatmap - Showing Activity on watching one TV show------------------
# We only want to only consider one TV show for this heatmap
user_fav_show = input("Enter TV Show Name you would like to see a heatmap for: ")
df = df[df['Show Name'] == user_fav_show]
# Using a new DF for the Heatmap, create a copy of the DF
df_heatmap = df.copy()
# group by month and year, get the sum
df_heatmap = df_heatmap.groupby(['Year', 'Month']).sum()
df_heatmap = df_heatmap.unstack(level=0)
# A sanity check
# print(df_heatmap)

# plot heatmap
sns.heatmap(df_heatmap,
            cmap="PuRd",
            annot=True,
            fmt="0.0f",
            vmin=1,
            vmax=70,
            linewidth=0.3,
            cbar_kws={'label': 'Duration (in Hours)'},
            annot_kws={"size": 10},
            )

plt.title(str(user_fav_show) + " Heatmap")
plt.xlabel("")
plt.ylabel("Month")
plt.suptitle("")
plt.tight_layout()
plt.show()
