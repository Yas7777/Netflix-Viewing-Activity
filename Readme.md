**Netflix Viewing Activity Visualization Project**

This idea was born out of my need to figure out how much Netflix I have consumed and what shows I have spent 
an obscene amount of time on. 

**Tools needed**

* Install Python 3
* An IDE of your choice
* CSV file of your Netflix Viewing Activity - Detailed instructions to download: https://help.netflix.com/en/node/101917

** How to **

**Graphs you will see:**

1 – Grouped Bar Graph by Profile

* **Details :** Illustrates how much each Netflix profile in your account has watched (in terms of duration minutes)
* **Image** (_my data for illustration purposes only)_
**_TODO:_**
[Graph 1](Figure_1.png)
* **Parameters:**  
  * X-Axis: Years
  * Y-Axis: Duration in minutes

2 – Stacked Bar Graph:

* **Details:** TV Shows watched vs Movies in terms of Duration (minutes) each year.
* **Image** (_my data for illustration purposes only)_
[Graph 2](Figure_2.png)
* **Parameters:**
  * X-Axis: Years
  * Y-Axis: Duration in minutes

3 - Horizontal Bar Graph

* **Details:** Top 10 TV shows watched in terms of Duration (minutes)
* **Image** (_my data for illustration purposes only)_
[Graph 3](Figure_3.png)
* **Parameters:**
  * X-Axis: Duration in minutes
  * Y-Axis: TV shows
* **Analysis**:  Friends is a comfort show that I have been a loyal fan of for a long time. This is a show I played on repeat, hence the high duration in this graph.

4 - Heatmap 

* **Details**: Heatmap of my viewing activity of Friends
* **Image** (_my data for illustration purposes only)_
[Graph 4](Figure_4.png)
* **Parameters:**
  * X-Axis: Years (does not contain data for 2020 as Friends left the Netflix USA platform)
  * Y-Axis: Months
* **Analysis:** Given that Graph 3 pointed out that Friends was the most-watched show, I wanted to understand how much time I spent watching that show over the years it was on Netflix and which month was my most highly watched. 

**Programming Language:**  Python 3
**Libraries used:** Pandas, Matplotlib, and Seaborn

**Source Data:** 
* Personal Netflix Activity downloaded through www.netflix.com
* Detailed instructions to download: https://help.netflix.com/en/node/101917

**🔥My Hot Takes🔥:** 
* The CSV file from Netflix requires significant clean-up to make it usable. 
* I did not use seaborn for stacked bar graphs as I found it particularly hard to use. 
* With every graph created, many sanity checks are needed to ensure that the data is correct. Some are included in this code, however, I have significantly condensed it here for readability and to ensure the focus is on the graphs.

**Future Improvements:** 
~~* Streamline data clean-up such that the code can be used for any user's data without amending the original code to account for that user's specific Netflix viewing activity.~~ 
* Include the IMDb library to see how ratings correlate with viewing activity.
* Include viewing activity data from other streaming platforms' data (HBO, Hulu, etc.)
