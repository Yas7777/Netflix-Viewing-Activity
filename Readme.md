# Netflix Viewing Activity Visualization Project

This idea was born out of my need to figure out how much Netflix I have consumed and what shows I have spent  an obscene amount of time on.   
What did version 1 contain  
What did version 2 contain  
  
# Table of Contents  
1. Installation and Tools
2. Programming Languages and libraries used
3. Data - cleanup
4. Graphs
5. My Hot Takes
6. Future Improvements
  
## Installation and Tools

* Install an IDE of your choice  
	> I prefer PyCharm: https://www.jetbrains.com/pycharm/download/
* Install  Python 3  
	> https://www.python.org/downloads/
* CSV file of your Netflix Viewing Activity
	> Detailed instructions to download: https://help.netflix.com/en/node/101917  

## Programming Languages and libraries used
* **Programming Language:** Python
* **Libraries used:** Pandas, Matplotlib, and Seaborn  

## Data - cleanup

*    
  
## Graphs

**1 - Grouped Bar Graph by Profile**  
  >* **Details :** Illustrates how much each Netflix profile in your account has watched (in terms of duration hours) 
  >* **Image** (_my data for illustration purposes only)_
  > [Graph 1](Figure_1.png)  
>* **Parameters:**
 >  * X-Axis: Years
 >  * Y-Axis: Duration in hours  
 
**2 – Stacked Bar Graph:**  
  
>* **Details:** TV Shows watched vs Movies in terms of Duration (hours) each year.  
>* **Image** (_my data for illustration purposes only)_  
[Graph 2](Figure_2.png)  
>* **Parameters:**  
>  * X-Axis: Years  
>  * Y-Axis: Duration in hours  
  
**3 - Horizontal Bar Graph**  
  
>* **Details:** Top 10 TV shows watched in terms of Duration (hours)  
>* **Image** (_my data for illustration purposes only)_  
[Graph 3](Figure_3.png)  
>* **Parameters:**  
  >  * X-Axis: Duration in minutes  
  >  * Y-Axis: TV shows  
  
**4 - Heatmap**   
  
>* **Details**: Heatmap of your viewing activity on a show of your choice  
>* **Image** (_my data for illustration purposes only)_  
[Graph 4](Figure_4.png)  
>* **Parameters:**  
  >  * X-Axis: Years   
  >  * Y-Axis: Months  
  
## 🔥My Hot Takes🔥

* The CSV file from Netflix requires significant clean-up to make it usable.   
* I did not use seaborn for stacked bar graphs as I found it particularly hard to use.   
* With every graph created, many sanity checks are needed to ensure that the data is correct. Some are included in this code, however, I have significantly condensed it here for readability and to ensure the focus is on the graphs.  

## Future Improvements

* ~~Streamline data clean-up such that the code can be used for any user's data without amending the original code to account for that user's specific Netflix viewing activity.~~
* Include the IMDb library to see how ratings correlate with viewing activity.  
* Include viewing activity data from other streaming platforms' data (HBO, Hulu, etc.)
