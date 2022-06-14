**My Netflix Viewing Activity Visualization Project**

I was interested to see my Netflix viewing activity since I have been using Netflix for over six years. 
The entire project used pandas, matplotlib, and seaborn. 

1 – Grouped Bar Graph by Profile

* **Details :** Illustrates how much each Netflix account watched (in terms of duration minutes) from 2016 to 2021. 
* **Image:**
[Graph 1](Figure_1.png)
* **Parameters:**  
  * X-Axis: Shows years 2016 through 2021. 2015 and 2022 are not included as the data for those years were incomplete, and I wanted the graphs to portray a complete data set. 
  * Y-Axis: Shows duration in minutes.
* **Parameters:**  My viewing frequency is significantly higher than the other profile. This is because TV watching is a hobby and relaxation activity for me. I like keeping up with new shows as they come out. The "binge" factor of shows has also severely contributed to my high duration.

2 – Stacked Bar Graph:

* **Details:** TV Shows watched vs Movies in terms of Duration (minutes) each year.
* **Image:**
[Graph 2](Figure_2.png)
* **Parameters:**
  * X-Axis: Shows years 2016 through 2021. 2015 and 2022 are not included as the data for those years were incomplete, and I wanted the graphs to portray a complete data set. 
  * Y-Axis: Shows duration in minutes.
* **Analysis**:  Netflix's movie collection slowly started shifting to original movie content which I found boring. I don't particularly appreciate wasting time on lousy entertainment when many other options are available. I also enjoy the episodic nature of TV shows more.

3 - Horizontal Bar Graph

* **Details:** Top 10 TV shows watched in terms of Duration (minutes)
* **Image:**
[Graph 3](Figure_3.png)
* **Parameters:**
  * X-Axis: Shows duration in minutes. 
  * Y-Axis: TV shows
* **Analysis**:  Friends is a comfort show that I have been a loyal fan of for a long time. This is a show I played on repeat, hence the high duration in this graph.

4 - Heatmap 

* **Details**: Heatmap of my viewing activity of Friends
* **Image:**
[Graph 4](Figure_4.png)
* **Parameters:**
  * X-Axis: Years (does not contain data for 2020 as Friends left the Netflix USA platform)
  * Y-Axis: Months
* **Analysis:** Given that Graph 3 pointed out that Friends was the most-watched show, I wanted to understand how much time I spent watching that show over the years it was on Netflix over the years and which month was my most highly watched. 

**Programming Language:**  Python 3

**Source Data:** 
* Personal Netflix Activity downloaded through www.netflix.com
* Detailed instructions to download: https://help.netflix.com/en/node/101917

**🔥My Hot Takes🔥:** 
* The CSV file from Netflix requires significant clean-up to make it usable. 
* I did not use seaborn for stacked bar graphs as I found it particularly hard to use. 
* With every graph created, many sanity checks are needed to ensure that the data is correct. Some are included in this code, however, I have significantly condensed it here for readability and to ensure the focus is on the graphs.

**Future Improvements:** 
* Streamline data clean-up such that the code can be used for any user's data without amending the original code to account for that user's specific Netflix viewing activity. 
* Include the IMDb library to see how ratings correlate with viewing activity.
* Include viewing activity data from other streaming platforms' data (HBO, Hulu, etc.)
