# IA626
In the first part of my project I wrote some code:
<br>
```python
starttime = time.time()
fn = 'trip_data_12.csv'
#fn = 'subset_data_12.csv'

f2 = open('subset_data_12.csv','w')
f2.write("")
f2.close()

f = open(fn, "r")
reader = csv.reader(f)
f2 = open('subset_data_12.csv','a')
writer = csv.writer(f2, delimiter=',', lineterminator='\n')
```
![Passenger count per hour](images/passenger_count_per_hour_plot.png)
