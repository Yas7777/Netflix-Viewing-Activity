import pandas as pd
import matplotlib.pyplot as plt
from imdb import IMDb
import pickle
import numpy as np
import seaborn as sns

# netflix file
netflix = '/Users/yasmeen/Downloads/netflix-report/CONTENT_INTERACTION/ViewingActivity.csv'
# read the file
df = pd.read_csv(netflix)
# remove Supplemental Video Type coloumn
del df['Supplemental Video Type']
'''
# duration = "00:21:12"
# Convert to minutes = first split the duration into a list by removing ":"
df['duration_minutes'] = df['Duration'].str.split(':')
# Convert to minutes = second i[0]*60 + i[1]
df['duration_minutes'] = df['duration_minutes'].apply(lambda x: int(x[0]) * 60 + int(x[1]))
# filter duration time to only more than 10
df = df[df['duration_minutes'] >= 10]'''

# make a new dataframe'''

sns.palplot(['#221f1f', '#b20710', '#e50914','#f5f5f1'])
plt.title("Netflix brand palette",loc='left',fontfamily='serif',fontsize=15,y=1.2)
dfl = df[df['Profile Name'] == 'Yasmeen']

x = dfl.groupby(['Type'])['Type'].count()
y = len(dfl)
r = ((x/y)).round(2)
mf_ratio = pd.DataFrame(r).T

fig, ax = plt.subplots(1, 1, figsize=(6.5, 2.5))
ax.barh(mf_ratio.index, mf_ratio['Movie'],
        color='#b20710', alpha=0.9, label='Male')
ax.barh(mf_ratio.index, mf_ratio['TV'], left=mf_ratio['Movie'],
        color='#221f1f', alpha=0.9, label='Female')
ax.set_xlim(0, 1)
ax.set_xticks([])
ax.set_yticks([])

'''
#annotating code starts here
for i in mf_ratio.index:
    ax.annotate(f"{int(mf_ratio['Movie'][i]*100)}%",
                   xy=(mf_ratio['Movie'][i]/2, i),
                   va = 'center', ha='center',fontsize=40, fontweight='light', fontfamily='serif',
                   color='white')
    ax.annotate("Movie",
                   xy=(mf_ratio['Movie'][i]/2, -0.25),
                   va = 'center', ha='center',fontsize=15, fontweight='light', fontfamily='serif',
                   color='white')
for i in mf_ratio.index:
    ax.annotate(f"{int(mf_ratio['TV'][i]*100)}%",
                xy=(mf_ratio['Movie'][i]+mf_ratio['TV'][i]/2,i),
                va = 'center', ha='center',fontsize=40, fontweight='light', fontfamily='serif',
                color='white')
    ax.annotate("TV",
                   xy=(mf_ratio['Movie'][i]+mf_ratio['TV'][i]/2, -0.25),
                   va = 'center', ha='center',fontsize=15, fontweight='light', fontfamily='serif',
                   color='white')

fig, ax = plt.subplots(1,1,figsize=(6.5,2.5))
ax.barh(mf_ratio.index, mf_ratio['Movie'],
        color='#b20710', alpha=0.9, label='Male')
ax.barh(mf_ratio.index, mf_ratio['TV'], left=mf_ratio['Movie'],
        color='#221f1f', alpha=0.9, label='Female')
ax.set_xlim(0, 1)
ax.set_xticks([])
ax.set_yticks([])


for i in mf_ratio.index:
    ax.annotate(f"{int(mf_ratio['Movie'][i]*100)}%",
                   xy=(mf_ratio['Movie'][i]/2, i),
                   va = 'center', ha='center',fontsize=40, fontweight='light', fontfamily='serif',
                   color='white')
    ax.annotate("Movie",
                   xy=(mf_ratio['Movie'][i]/2, -0.25),
                   va = 'center', ha='center',fontsize=15, fontweight='light', fontfamily='serif',
                   color='white')
for i in mf_ratio.index:
    ax.annotate(f"{int(mf_ratio['TV'][i]*100)}%",
                xy=(mf_ratio['Movie'][i]+mf_ratio['TV'][i]/2,i),
                va = 'center', ha='center',fontsize=40, fontweight='light', fontfamily='serif',
                color='white')
    ax.annotate("TV",
                   xy=(mf_ratio['Movie'][i]+mf_ratio['TV'][i]/2, -0.25),
                   va = 'center', ha='center',fontsize=15, fontweight='light', fontfamily='serif',
                   color='white')''''''

fig.text(0.125,1.0,'Movie & TV Show distribution',fontfamily='serif',fontsize=15,fontweight='bold')
fig.text(0.125,0.90,'I watch way more TV than movies on NFLX.',fontfamily='serif',fontsize=12,fontweight='light')
for s in ['top','left','right','bottom']:
    ax.spines[s].set_visible(False)
ax.legend().set_visible(False)
plt.show()

dfl.sample()'''
# create a graph for duration of each profile
profile_count = dfl["Profile Name"].value_counts()
plt.figure(figsize=(8,5))
plt.bar(profile_count.index, profile_count.values, color="pink")
plt.ylabel("Freq", fontsize=14)
plt.xlabel("Profile Names", fontsize=14)
plt.xticks(fontsize=11)
plt.title("Viewing Frequency of Each Profile", fontsize=16)
plt.show()

fig, ax = plt.subplots(1,1,figsize=(6.5,2.5))
ax.barh(mf_ratio.index, mf_ratio['Movie'],
        color='#b20710', alpha=0.9, label='Male')
ax.barh(mf_ratio.index, mf_ratio['TV'], left=mf_ratio['Movie'],
        color='#221f1f', alpha=0.9, label='Female')
ax.set_xlim(0, 1)
ax.set_xticks([])
ax.set_yticks([])

fig, ax = plt.subplots(1,1,figsize=(6.5,2.5))
ax.barh(mf_ratio.index, mf_ratio['Movie'],
        color='#b20710', alpha=0.9, label='Male')
ax.barh(mf_ratio.index, mf_ratio['TV'], left=mf_ratio['Movie'],
        color='#221f1f', alpha=0.9, label='Female')
ax.set_xlim(0, 1)
ax.set_xticks([])
ax.set_yticks([])

fig.text(0.125,1.0,'Movie & TV Show distribution',fontfamily='serif',fontsize=15,fontweight='bold')
fig.text(0.125,0.90,'I watch way more TV than movies on NFLX.',fontfamily='serif',fontsize=12,fontweight='light')
for s in ['top','left','right','bottom']:
    ax.spines[s].set_visible(False)
ax.legend().set_visible(False)
plt.show()

# create and instance of the IMDb class
from imdb import IMDb
ia = IMDb()
ia.get_movie_infoset()
shows = ia.search_movie('Black Mirror')
print (shows)
print(shows[0]['kind'])
print (shows[0])
show = ia.get_movie(shows[0].movieID)
print('Genres:')
print(*show["genres"], sep="/")